import argparse
import json
import math
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field

LOCAL_STOP_MARKERS = ("\nUser", "\nAssistant", "<think", "</think")
META_TOKEN_MARKERS = ("User", "Assistant", "Instruction", "<think", "</think", "<|")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Explore low-confidence generation branches from a local Ollama model."
    )
    parser.add_argument(
        "--host",
        default="http://127.0.0.1:11434",
        help="Base URL for the Ollama server.",
    )
    parser.add_argument(
        "--model",
        default="qwen3.5:latest",
        help="Model name to run.",
    )
    parser.add_argument(
        "--prompt",
        default="Write one short sentence about why tea is nice.",
        help="Prompt to send to the model.",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=24,
        help="Maximum generated tokens per branch.",
    )
    parser.add_argument(
        "--top-logprobs",
        type=int,
        default=5,
        help="How many alternative token logprobs to request from Ollama.",
    )
    parser.add_argument(
        "--weak-prob",
        type=float,
        default=0.5,
        help="Branch when the chosen token probability is below this value.",
    )
    parser.add_argument(
        "--min-branch-prob",
        type=float,
        default=0.02,
        help="Ignore alternatives below this probability when branching.",
    )
    parser.add_argument(
        "--max-nodes",
        type=int,
        default=200,
        help="Maximum token-expansion calls across the whole search.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=120.0,
        help="Request timeout in seconds.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.0,
        help="Sampling temperature. Use 0 for stable branching.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=7,
        help="Seed passed to Ollama for repeatable sampling when supported.",
    )
    parser.add_argument(
        "--mode",
        choices=("tree", "single"),
        default="tree",
        help="Use 'tree' to explore low-confidence branches or 'single' for a normal response.",
    )
    parser.add_argument(
        "--show-paths",
        action="store_true",
        help="Print the token-by-token path for each completed branch.",
    )
    return parser.parse_args()


@dataclass
class TokenChoice:
    token: str
    logprob: float
    source: str

    @property
    def prob(self) -> float:
        if self.logprob is None:
            return 0.0
        if self.logprob < -700:
            return 0.0
        return math.exp(self.logprob)


@dataclass
class BranchState:
    text: str = ""
    steps: list[TokenChoice] = field(default_factory=list)
    cumulative_logprob: float = 0.0

    def with_choice(self, choice: TokenChoice) -> "BranchState":
        return BranchState(
            text=self.text + choice.token,
            steps=self.steps + [choice],
            cumulative_logprob=self.cumulative_logprob + (choice.logprob or 0.0),
        )


@dataclass
class CompletedBranch:
    text: str
    steps: list[TokenChoice]
    cumulative_logprob: float
    stop_reason: str


@dataclass
class TreeNode:
    token: str
    prob: float | None = None
    source: str | None = None
    stop_reasons: list[str] = field(default_factory=list)
    children: dict[str, "TreeNode"] = field(default_factory=dict)


def trim_local_stop_markers(text: str) -> tuple[str, str | None]:
    cut_index = None
    matched_marker = None

    for marker in LOCAL_STOP_MARKERS:
        index = text.find(marker)
        if index == -1:
            continue
        if cut_index is None or index < cut_index:
            cut_index = index
            matched_marker = marker

    if cut_index is None:
        return text, None
    return text[:cut_index].rstrip(), matched_marker


def is_meta_token(token: str) -> bool:
    stripped = token.strip()
    if not stripped:
        return False
    return any(marker in stripped for marker in META_TOKEN_MARKERS)


def build_tree(completed: list[CompletedBranch]) -> TreeNode:
    root = TreeNode(token="<root>")

    for branch in completed:
        node = root
        for step in branch.steps:
            child = node.children.get(step.token)
            if child is None:
                child = TreeNode(
                    token=step.token,
                    prob=step.prob,
                    source=step.source,
                )
                node.children[step.token] = child
            node = child
        node.stop_reasons.append(branch.stop_reason)

    return root


def summarize_stop_reasons(stop_reasons: list[str]) -> str:
    if not stop_reasons:
        return ""
    unique = list(dict.fromkeys(stop_reasons))
    if len(unique) == 1:
        return unique[0]
    return ", ".join(unique)


def render_token_label(node: TreeNode, is_variant: bool) -> str:
    token = repr(node.token)
    if is_variant:
        token = f"<<{token}>>"

    details = []
    if node.prob is not None:
        details.append(f"p={node.prob:.3f}")
    if node.source:
        details.append(node.source)
    if node.stop_reasons:
        details.append(f"stop={summarize_stop_reasons(node.stop_reasons)}")

    if details:
        return f"{token} [{' | '.join(details)}]"
    return token


def print_tree(node: TreeNode, prefix: str = "", is_root: bool = True) -> None:
    if is_root:
        print("\nTree:")
        print("ROOT")

    children = list(node.children.values())
    children.sort(
        key=lambda child: (
            child.prob is None,
            -(child.prob or 0.0),
            child.token,
        )
    )

    child_count = len(children)
    for index, child in enumerate(children):
        is_last = index == child_count - 1
        connector = "`- " if is_last else "|- "
        is_variant = child_count > 1
        print(f"{prefix}{connector}{render_token_label(child, is_variant)}")
        next_prefix = prefix + ("   " if is_last else "|  ")
        print_tree(child, prefix=next_prefix, is_root=False)


def post_json(url: str, payload: dict, timeout: float) -> dict:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from Ollama: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Could not reach Ollama. Make sure the app/server is running on "
            f"{url.rsplit('/api/', 1)[0]}"
        ) from exc


def make_raw_prompt(user_prompt: str, current_text: str) -> str:
    # Keep the wrapper stable so each request predicts the next assistant token.
    return (
        "Instruction: Continue only the assistant reply. "
        "Do not emit role labels, XML-like think tags, or extra scaffolding.\n"
        f"User: {user_prompt}\n"
        f"Assistant:{current_text}"
    )


def request_single_token(args: argparse.Namespace, current_text: str) -> dict:
    payload = {
        "model": args.model,
        "prompt": make_raw_prompt(args.prompt, current_text),
        "stream": False,
        "raw": True,
        "think": False,
        "logprobs": True,
        "top_logprobs": args.top_logprobs,
        "options": {
            "temperature": args.temperature,
            "num_predict": 1,
            "seed": args.seed,
            "stop": ["\nUser:", "\nAssistant:", "<think>", "</think>"],
        },
    }
    return post_json(
        f"{args.host.rstrip('/')}/api/generate",
        payload,
        timeout=args.timeout,
    )


def unique_choices(item: dict, min_branch_prob: float) -> list[TokenChoice]:
    choices: list[TokenChoice] = []
    seen_tokens: set[str] = set()

    primary = TokenChoice(
        token=item.get("token", ""),
        logprob=item.get("logprob"),
        source="chosen",
    )
    choices.append(primary)
    seen_tokens.add(primary.token)

    for alt in item.get("top_logprobs") or []:
        token = alt.get("token", "")
        if token in seen_tokens:
            continue
        choice = TokenChoice(
            token=token,
            logprob=alt.get("logprob"),
            source="alternative",
        )
        if choice.prob < min_branch_prob:
            continue
        choices.append(choice)
        seen_tokens.add(token)

    choices.sort(key=lambda choice: choice.logprob, reverse=True)
    return choices


def run_single(args: argparse.Namespace) -> int:
    payload = {
        "model": args.model,
        "prompt": args.prompt,
        "stream": False,
        "think": False,
        "logprobs": True,
        "top_logprobs": args.top_logprobs,
        "options": {
            "temperature": args.temperature,
            "num_predict": args.max_tokens,
            "seed": args.seed,
            "stop": ["<think>", "</think>"],
        },
    }
    response = post_json(
        f"{args.host.rstrip('/')}/api/generate",
        payload,
        timeout=args.timeout,
    )

    print(f"Model: {response.get('model', args.model)}")
    print(f"Done reason: {response.get('done_reason', 'unknown')}")
    print(f"Prompt tokens: {response.get('prompt_eval_count', 'n/a')}")
    print(f"Generated tokens: {response.get('eval_count', 'n/a')}")
    print("\nResponse:\n")
    print(response.get("response", "").strip() or "<empty response>")

    logprobs = response.get("logprobs") or []
    if logprobs:
        print("\nToken logprobs:")
        for index, item in enumerate(logprobs, start=1):
            token = item.get("token", "")
            logprob = item.get("logprob")
            prob = math.exp(logprob) if logprob is not None and logprob > -700 else 0.0
            print(f"{index:>3}. token={token!r} prob={prob:.6f} logprob={logprob}")
    return 0


def explore_tree(args: argparse.Namespace) -> int:
    frontier = [BranchState()]
    completed: list[CompletedBranch] = []
    explored_nodes = 0

    while frontier:
        state = frontier.pop()

        while True:
            if explored_nodes >= args.max_nodes:
                completed.append(
                    CompletedBranch(
                        text=state.text,
                        steps=state.steps,
                        cumulative_logprob=state.cumulative_logprob,
                        stop_reason="max_nodes",
                    )
                )
                frontier.clear()
                break

            if len(state.steps) >= args.max_tokens:
                completed.append(
                    CompletedBranch(
                        text=state.text,
                        steps=state.steps,
                        cumulative_logprob=state.cumulative_logprob,
                        stop_reason="max_tokens",
                    )
                )
                break

            response = request_single_token(args, state.text)
            explored_nodes += 1
            token_items = response.get("logprobs") or []
            token_text = response.get("response", "")
            done_reason = response.get("done_reason", "unknown")

            if not token_items or token_text == "":
                completed.append(
                    CompletedBranch(
                        text=state.text,
                        steps=state.steps,
                        cumulative_logprob=state.cumulative_logprob,
                        stop_reason=done_reason,
                    )
                )
                break

            choices = unique_choices(token_items[0], args.min_branch_prob)
            best_choice = choices[0]

            if best_choice.token != token_text:
                # Prefer the actual generated token if it differs from top_logprobs order.
                for choice in choices:
                    if choice.token == token_text:
                        best_choice = TokenChoice(
                            token=choice.token,
                            logprob=choice.logprob,
                            source="chosen",
                        )
                        break
                else:
                    best_choice = TokenChoice(
                        token=token_text,
                        logprob=token_items[0].get("logprob"),
                        source="chosen",
                    )

            if is_meta_token(best_choice.token):
                completed.append(
                    CompletedBranch(
                        text=state.text.rstrip(),
                        steps=state.steps,
                        cumulative_logprob=state.cumulative_logprob,
                        stop_reason=f"meta_token:{best_choice.token}",
                    )
                )
                break

            filtered_choices = [best_choice]
            for choice in choices:
                if choice.token == best_choice.token:
                    continue
                if is_meta_token(choice.token):
                    continue
                filtered_choices.append(choice)

            branch_choices = [best_choice]
            if best_choice.prob < args.weak_prob:
                branch_choices = []
                for choice in filtered_choices:
                    if choice.prob >= args.min_branch_prob:
                        branch_choices.append(choice)
                if not branch_choices:
                    branch_choices = [best_choice]

            for alternative in reversed(branch_choices[1:]):
                frontier.append(state.with_choice(alternative))

            state = state.with_choice(branch_choices[0])
            trimmed_text, matched_marker = trim_local_stop_markers(state.text)
            if matched_marker is not None:
                completed.append(
                    CompletedBranch(
                        text=trimmed_text,
                        steps=state.steps,
                        cumulative_logprob=state.cumulative_logprob,
                        stop_reason=f"stop_marker:{matched_marker}",
                    )
                )
                break

    completed.sort(key=lambda branch: branch.cumulative_logprob, reverse=True)

    print(f"Model: {args.model}")
    print(f"Prompt: {args.prompt!r}")
    print(f"Weak-prob threshold: {args.weak_prob}")
    print(f"Explored nodes: {explored_nodes}")
    print(f"Completed branches: {len(completed)}")
    print("Highlighted tokens with <<...>> are branch variants at that point in the tree.")
    print_tree(build_tree(completed))

    print("\nLeaves:")
    for index, branch in enumerate(completed, start=1):
        avg_prob = 0.0
        if branch.steps:
            avg_prob = math.exp(branch.cumulative_logprob / len(branch.steps))
        print(
            f"{index:>2}. text={branch.text!r} "
            f"[tokens={len(branch.steps)} avg_p={avg_prob:.3f} stop={branch.stop_reason}]"
        )

        if args.show_paths:
            print("    path:")
            for step_number, step in enumerate(branch.steps, start=1):
                print(
                    "      "
                    f"{step_number:>2}. token={step.token!r} prob={step.prob:.6f} "
                    f"source={step.source}"
                )

    return 0


def main() -> int:
    args = parse_args()
    if args.mode == "single":
        return run_single(args)
    return explore_tree(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
