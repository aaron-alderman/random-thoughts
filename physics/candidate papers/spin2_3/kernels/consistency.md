# Consistency Kernel

## Purpose

This document is the consistency source text for the project.

It is not a paper draft. It is the place where all constraint-type questions are kept together inside one domain. The job of this file is to say:

- what conditions the framework must satisfy to count as coherent
- which claims are forced once the setup is fixed
- which claims are only attractive possibilities
- where the strongest proof burdens live

This file is where "what follows naturally" gets translated into "what is actually forced by the stated assumptions and constraints."

---

## Scope

This file covers:

- positivity, trace preservation, and stability of the reduced dynamics
- anomaly-based constraints on matter content
- uniqueness or non-uniqueness questions
- generation-counting burdens
- the difference between constrained fitting and genuine derivation

This file does not cover:

- the initial construction of the static spaces
- the full dynamical derivation itself
- interpretive claims unless they affect consistency
- quantitative phenomenology

---

## Core consistency question

The central question is:

> Once the framework's postulates and structural choices are fixed, what is genuinely permitted, required, excluded, or still underdetermined?

Consistency is where aesthetic language should give way to precise burden:

- required
- allowed
- excluded
- unresolved

---

## Types of consistency in the project

There are at least four distinct kinds of consistency here.

### C1. Algebraic consistency

- are the stated representations and decompositions mathematically well-defined?
- do the subgroup embeddings and charge assignments make sense inside the chosen structures?

### C2. Dynamical consistency

- is the reduced dynamics positive?
- is it trace preserving?
- is it stable in the regime where it is claimed?

### C3. Gauge-theoretic consistency

- is the proposed matter content anomaly free?
- what additional states are forced if a partial matter content is anomalous?

### C4. Selection consistency

- when does a construction become unique rather than merely convenient?
- when is something excluded rather than simply not yet found?

The framework uses all four, and they should not be blurred together.

---

## Reduced-dynamics consistency

In the weak-coupling Markov regime, the reduced `T1` dynamics is intended to take Lindblad form.

If that derivation is valid, then the safe consequences are:

- trace preservation
- complete positivity
- stability in the semigroup sense

The key consistency point is conditional:

- these properties are not asserted absolutely
- they are asserted **within the reduction regime**

So the kernel form is:

- the reduced dynamics is consistent provided the Markovian reduction is justified

This prevents overstating what has actually been shown.

### Channel-selection consistency

There is also a narrower consistency issue before one even reaches the Markov regime:

- does the selected direction define one direct zero-mass channel, or more than one?

In the current reduction picture, the hidden line splits into two charge sectors that are exchanged by

$$
u \mapsto -u.
$$

So they are best read as the two opposite orientations of the same hidden line. Once phase covariance has forced the parent zero-mass operator to be charge diagonal,

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-} + h_+ P_{\Pi,+},
$$

the remaining possibilities are:

- `h_- = h_+`: direct traversal is blind to the orientation of `u`
- `h_- \neq h_+` with both nonzero: direct traversal uses two oriented channels
- exactly one nonzero coefficient: direct traversal uses one oriented channel

If the framework wants both of the following:

1. the selected direction `u` to remain physically meaningful as an oriented choice
2. the observable zero-mass channel to be unique

then one-sector traversal is the minimal selection-consistent outcome.

This does not yet prove one-sector traversal from pure mathematics alone. But it does show that, within the current architecture, one-sector support is not an arbitrary embellishment. It is the only option that preserves both oriented directionality and a unique direct readout channel.

There is also a further narrowing of the remaining ambiguity. After the parent-adapted basis conditions are imposed, the only nontrivial residual freedom is the simultaneous global orientation reversal of hidden line and time direction. So the consistency problem is no longer "which of many reductions should be chosen?" It is:

- which global orientation should count as the physical forward/readout orientation?

This is useful because it localizes the unfinished work. Pure algebra does not obviously remove that last `\mathbf Z_2`; the best current route is to tie it to the same forward semigroup/readout arrow that defines the observable sector in the reduced theory.

So the consistency question can now be written more sharply:

- does the same sector carry direct zero-mass support, observable readout, and forward reduced semigroup evolution?

If yes, the residual global orientation is fixed consistently.
If not, the framework would be assigning incompatible meanings to its last remaining `\mathbf Z_2` choice.

The transport system suggests one more consistency check of the same type:

- in the phase normalization where the direct readout branch sits at `\Phi_*=0`, does that same sector lie on the constructive/persistent side, hence have `\kappa_u > 0`?

If yes, the residual orientation is being fixed coherently by readout, semigroup direction, and transport stability all at once.
If not, the framework would be mixing incompatible orientation conventions across its static, dynamical, and epistemic layers.

So the consistency problem has effectively collapsed to one final question:

- is the unique direct readout channel required to be the constructive/persistent one?

If yes, then the same rule fixes:

- which parent orientation is physical
- which reduced block is called `T1`
- which sector carries direct zero-mass support
- which sector carries forward observable evolution

If not, then the last `\mathbf Z_2` remains genuinely free and the current `T1` identification stays only conditionally fixed.

---

## Matter-content consistency

On the static side, if one identifies a left-handed matter sector from the `T1` construction, then anomaly cancellation becomes a major selection rule.

The safe logic is:

1. propose the left-handed matter content from the static construction
2. compute the anomaly conditions
3. determine what additional content is required for consistency

What anomaly cancellation can safely do:

- rule out inconsistent partial spectra
- constrain what additional right-handed states are needed

What it does **not** automatically do:

- prove that the framework itself generated those states geometrically

That distinction is crucial. Consistency constraints can force completion of a spectrum without thereby proving that the missing states arise from the same geometric mechanism.

The topological comparison should also be phrased carefully. The DIII boundary story may capture a lower-dimensional parity/global shadow of the same `T1` matter content, but it does not by itself replace the full four-dimensional gauge-anomaly calculation. See `kernels/diii-anomaly-bridge.md`.

---

## Hypercharge and uniqueness

One of the strongest consistency questions in the project is:

- is the hypercharge construction unique?

The current kernel supports the following careful statement:

- within the ansatz `Y = a J^{01} + b Q7`, matching the target doublet charges can fix `a` and `b`

The new branching note sharpens this further on the bare left-handed seed `T1 \otimes (\mathbf 3 \oplus \mathbf 1)`. If `Q7` is taken to be the natural `SU(3)`-invariant traceless grading on `\mathbf 3 \oplus \mathbf 1`,
$$
Q7 = \mathrm{diag}\!\left(\frac13,\frac13,\frac13,-1\right),
$$
then matching the left-handed quark/lepton doublet charges gives
$$
Y\big|_{T1 \otimes (\mathbf 3 \oplus \mathbf 1)} = \frac12\,Q7
$$
and leaves no visible `J^{01}` contribution on that restricted seed, because `J^{01}` is constant on `T1`.

This is a meaningful internal constraint result.

But the stronger statements require more proof:

- that the first obvious enlargement `(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)` is not already sufficient
- that the same coefficient choice survives extension to right-handed or otherwise enlarged sectors
- that this ansatz is itself canonical
- that no other natural internal grading could do the same job
- that the resulting `U(1)` is unique in the strongest physical sense

The new screening note `kernels/right-handed-completion-screening.md` now closes that first enlargement check. Under the current `SU(3) x K` reading, the doubled trial carrier
$$
(T1 \oplus T2) \otimes (\mathbf 3 \oplus \mathbf 1)
$$
contains only weak doublets, so it cannot literally be the right-handed singlet completion. Moreover, once the left-handed `T1` charges are fixed, the same doubled space still forces
$$
a = 0,
\qquad
b = \frac12,
$$
so `J^{01}` remains invisible there as an independent hypercharge ingredient.

The next note `kernels/minimal-right-handed-singlet-candidate.md` then identifies the first algebraic repair that does work at the representation level: add one extra weak doublet factor `S_aux`. On the weak-singlet sector of
$$
(T1 \oplus T2) \otimes S_{\mathrm{aux}} \otimes (\mathbf 3 \oplus \mathbf 1),
$$
the same hypercharge ansatz reproduces the standard one-generation right-handed singlet charges with
$$
Y = J^{01} + \frac12 Q7
$$
up to the global orientation flip. So `J^{01}` does become genuinely useful there.

But that immediately exposes the next tension: the bare left-handed seed wanted `a=0`, while the minimal singlet candidate wants `|a|=1`. So the live problem is no longer whether `J^{01}` can ever matter. It is how the left-handed and right-handed sectors are embedded so that one global `Y` operator works across both.

The next test note `kernels/unified-carrier-hypercharge-test.md` now checks the smallest natural carrier containing both types of slots at once,
$$
(T1 \oplus T2) \otimes (\mathbf 1 \oplus S_{\mathrm{aux}}) \otimes (\mathbf 3 \oplus \mathbf 1),
$$
with neutral `S_{\mathrm{aux}}`. That unified carrier is large enough to contain both left-handed-shaped doublets and right-handed-shaped singlets, but it still gives a finite no-go:
$$
\text{left-handed fit} \Longrightarrow a=0,\; b=\frac12,
$$
while
$$
\text{right-handed fit} \Longrightarrow a=\pm 1,\; b=\frac12.
$$
So the neutral-`S_{\mathrm{aux}}` unified carrier still cannot support one global `Y = a J^{01} + b Q7`.

The next note `kernels/unified-carrier-projector-fix.md` then shows that this is not the end of the algebraic story. Since `S_{\mathrm{aux}}` is an irreducible weak doublet, there is no nontrivial `SU(2)`-commuting grading on `S_{\mathrm{aux}}` alone. But there is a natural commuting projector on the reducible block `\mathbf 1 \oplus S_{\mathrm{aux}}`, namely `P_{\mathrm{aux},0}` onto the trivial summand. Enlarging the hypercharge operator to
$$
Y = a J^{01} + b Q7 + c P_{\mathrm{aux},0}
$$
gives the exact fit
$$
Y = J^{01} + \frac12 Q7 + \frac12 P_{\mathrm{aux},0}
$$
in the current orientation on the selected left-handed and right-handed slots. So the smallest unified-carrier obstruction is repaired at the slot level by one projector term.

The follow-up note `kernels/even-line-exotic-branch-obstruction.md` then shows the first remaining spectrum-level gap. The same auxiliary even line that supplies the desired `T1` left-handed doublets also carries the complementary `T2` branch, and that branch gives exotic weak doublets
$$
(\mathbf 3,\mathbf 2)_{7/6}
\oplus
(\mathbf 1,\mathbf 2)_{1/2}.
$$
So the projector repair is not yet a full carrier closure. It still needs a branch-selection, quotient, or decoupling mechanism on the even auxiliary sector.

The next note `kernels/minimal-physical-subcarrier-candidate.md` then turns that complaint into a concrete operator-level proposal. Instead of treating the full tensor product as physical, it defines the minimal correlated subcarrier
$$
P_{\mathrm{phys}}
=
P_{T1}P_{\mathrm{aux},0}
\;+\;
P_{\mathrm{odd},0}P_{\mathrm{aux},1},
$$
with `P_{T1}` the `T1` branch projector on the even auxiliary line and `P_{\mathrm{odd},0}` the weak-singlet projector on the odd auxiliary sector. This is the first candidate that removes both the complementary even-branch doublets and the odd weak-triplet channels at the representation level.

The follow-up note `kernels/branch-casimir-superselection-candidate.md` then repackages that same subcarrier in the cleanest language currently available. The even-line piece is exactly the observable-sector projector already isolated by the orientation/readout programme, while the odd-line piece is the minimal total weak-spin projector. So the candidate physical space can now be read as
$$
P_{\mathrm{phys}}
=
P_{\mathrm{obs}}P_{\mathrm{aux},0}
\;+\;
P_{j_{\min}}P_{\mathrm{aux},1},
$$
namely observable-branch selection on the even line plus minimal-Casimir selection on the odd line. This is the first point where the carrier proposal begins to look like a genuine superselection rule rather than a repair assembled from unrelated slot choices.

The next refinement note `kernels/odd-sector-epsilon-channel.md` then sharpens the odd half one step further. On `\mathbf 2 \otimes \mathbf 2`, the weak singlet is exactly the antisymmetric channel
$$
\wedge^2(\mathbf 2) \cong \mathbf 1,
$$
cut out by the unique invariant tensor `\epsilon_{ab}`. Equivalently,
$$
P_{\epsilon}
=
\frac12(\mathbf 1 - \tau)
=
\mathbf 1 - \frac12 C_{\mathrm{tot}}.
$$
So the odd-sector rule is no longer best read as an arbitrary low-spin preference. It is the standard invariant antisymmetric scalar-pairing channel. This makes the odd selector much less mysterious than the even one.

The next refinement note `kernels/even-sector-observable-projector-descent.md` does the analogous cleanup on the even side. The even-line selector in the physical-subcarrier candidate is not a new hypercharge-specific branch rule. It is exactly the reduced observable/readout-sector projector already built into the ambient scaffold:
$$
\mathcal R_{\mathrm{op}}(P_{\Pi,-}) = P_{\mathrm{obs}},
\qquad
P_{\mathrm{obs}} = P_{T1}
$$
once the physical orientation is fixed. So the even half of the carrier proposal is already the same one-sided support rule the zero-mass/readout descent programme needed independently.

The follow-up note `kernels/auxiliary-projector-casimir-rewrite.md` makes that projector less ad hoc. If the auxiliary block truly carries the reducible `SU(2)` representation `\mathbf 1 \oplus \mathbf 2`, then
$$
P_{\mathrm{aux},0} = \mathbf 1 - \frac43 C_{\mathrm{aux}}
$$
is exactly the Casimir-zero projector. So the fix is no longer basis-dependent bookkeeping; it becomes a standard representation-theoretic invariant of the auxiliary block.

The next screening note `kernels/quaternionic-auxiliary-block-screening.md` then checks the first obvious parent-side source candidate for that block: the existing local quaternionic slice `H(u,v)`. The result is negative but useful. Under the natural visible `SU(2)` action already used elsewhere in the scaffold, `H(u,v)` is the irreducible complex doublet `\mathbf 2`, not the reducible complex module `\mathbf 1 \oplus \mathbf 2`; and the familiar scalar-plus-imaginary decomposition of quaternions belongs instead to a different real adjoint action, giving `\mathbf 1 \oplus \mathbf 3`.

The next candidate note `kernels/auxiliary-vacuum-doublet-candidate.md` then gives the best current positive mechanism after that screen. If the existing quaternionic doublet `V \cong \mathbf 2` is given its standard fermionic completion, then
$$
\Lambda^\bullet V \cong \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1,
$$
and the low-occupancy sector
$$
\Lambda^0 V \oplus \Lambda^1 V \cong \mathbf 1 \oplus \mathbf 2
$$
is exactly the auxiliary block needed by the projector repair. In that reading, the fitted projector becomes the vacuum projector. That is structurally better than a bare direct sum, but it introduces a new sharp burden: explain why the relevant carrier is the vacuum-plus-single-occupancy sector rather than the full Fock space, or else explain the fate of the top wedge singlet `\Lambda^2 V \cong \mathbf 1`.

The next obstruction note `kernels/full-fock-auxiliary-obstruction.md` then shows why that low-occupancy qualifier matters. If one keeps the full completion
$$
\Lambda^\bullet V \cong \mathbf 1 \oplus \mathbf 2 \oplus \mathbf 1
$$
inside the current hypercharge fit, the top wedge `\Lambda^2 V` does not produce extra singlets. It produces extra weak doublets, and those doublets carry the right-handed-style hypercharge values `-1/3,-1` on the `T1` branch and `2/3,0` on the `T2` branch. So the full completion places the right hypercharge values on the wrong `SU(2)` representation type.

So the live burden has changed again. It is no longer to find any algebraic fix, or even to rewrite the fix canonically. It is to justify the upstream observable/readout selector and the low-occupancy auxiliary rule, because the carrier-level branch/antisymmetric-pairing structure itself is now comparatively disciplined.

So there are three different levels:

1. coefficients fixed within a chosen ansatz
2. ansatz preferred among nearby options
3. construction genuinely unique

The kernel should not collapse these into one claim.

---

## Generation-counting consistency

The generation story is especially burdened by strong claims.

Safe consistency statement:

- `J3(O)` supplies a natural three-slot structure

Stronger statement:

- those three slots correspond to exactly three physical generations

Stronger still:

- a fourth generation is genuinely excluded

The first is safe. The second and third require a much tighter chain of reasoning.

In particular, a formal algebraic bound on octonionic Jordan matrices is not automatically the same thing as a physical exclusion theorem unless the mapping from algebraic slots to physical generations is already watertight.

This is one of the biggest proof-burden hotspots in the whole framework.

---

## Constrained fit versus derivation

The framework repeatedly encounters a subtle issue:

- a structure may be strongly constrained by consistency without being fully derived

Examples:

- hypercharge coefficients
- right-handed content
- generation claims

The kernel should therefore track three distinct outcomes:

1. **derived**
   The result follows directly from the setup.

2. **consistency-forced**
   The result is required once one combines the setup with independent consistency conditions.

3. **selected by fitting**
   The result is chosen because it matches the intended target structure.

This distinction is essential for honest paper-writing.

---

## Consistency claim ledger

| Claim | Role | Level | Comment |
|---|---|---|---|
| the reduced Markovian generator is trace preserving in the Lindblad regime | derived under assumptions | 4 | conditional but strong |
| the reduced Markovian generator is completely positive in the Lindblad regime | derived under assumptions | 4 | same regime caveat |
| anomaly cancellation constrains the completion of the matter content | derived consistency condition | 3 | standard and important |
| the coefficients in `Y = a J^{01} + b Q7` can be fixed inside the chosen ansatz | constrained within ansatz | 4 | on the bare left-handed `T1 tensor (3 + 1)` seed, the natural `Q7` normalization gives `Y = (1/2)Q7`; the real remaining burden is extension beyond that seed |
| the hypercharge construction is uniquely canonical | strong consistency claim under development | 5 | needs more proof |
| exactly three generations are forced | strong claim under development | 5 | not yet safe as a theorem |
| a fourth generation is excluded in the physical theory | unresolved strong exclusion claim | 6 | major proof burden |

---

## NS Programme structural corroboration

This section records corroboration of key consistency claims from the NS/J3(O) regularity programme. All bridge identifications are structural proposals (Level 5). The underlying NS results are at Level 3–4.

---

### Jordan algebra positivity and reflection positivity

**What the NS programme established (Level 4):**

The NS programme establishes a filtering mechanism via the cubic norm of J3(O):

- N_lifted = N_local + α·b + β·b² where β = −X₃₃ = S₁₁ + S₂₂ − h
- Near Type I blow-up: β ~ a ~ (T*−t)⁻¹ > 0 (regularising)
- The condition N_lifted ≥ 0 is the positivity condition of the Jordan algebra positive cone
- Scaling contradiction: N_lifted ~ (T*−t)^{−7/2} from below vs N_lifted ≤ C(T*−t)^{−3} from the Type I bound; these are incompatible near T* if N_lifted ≥ 0 is dynamically preserved (exponent gap 1/2)
- C_eff = 0.022 ≪ 1/3 (N=32³, needs N=64³ confirmation): the NS flow is 15× inside the stable Raychaudhuri regime

**What this addresses here (Level 4):**

The reduced Markovian generator is claimed to be trace preserving and completely positive in the Lindblad regime. This positivity claim is conditional on the Markovian reduction being justified. The framework also needs to establish that the reduced projected dynamics preserves positivity in the appropriate regime.

**Proposed bridge identification (Level 5):**

The Jordan algebra positivity condition N_lifted ≥ 0 is mathematically equivalent to reflection positivity of the vorticity two-point function in the AdS₄/CFT₃ dual theory. Both are positivity conditions on the same algebraic object (the bilinear form defined by the two-point function); both are required for unitarity. Under this identification, NS regularity becomes equivalent to unitarity of the dual CFT₃, which is protected by representation theory of Spin(2,3).

The C_eff mapping: C_eff = 0.022 corresponds to an effective m²L² ≈ −0.15 in AdS₄ units (BF bound is −2.25 for d=3). The vorticity operator has conformal dimension Δ ≈ 2.95 in the dual CFT₃ — a nearly marginal operator. These are scaling arguments (Level 4–5), not derived equivalences.

**What this file still needs:**

A derivation within the Spin(2,3) setting that the reduced projected dynamics automatically satisfies the Jordan algebra positivity condition, or a proof that violation of positivity is inconsistent with the representation theory of Spin(2,3). This would close Gap A of the NS programme from the gauge-theory side.

---

### J3(O) vs J3(C⊗O): dimensional constraint from the consistency side

**Proposed bridge identification (Level 4):**

The NS dimensional count 15 + 12 = 27 bears on the consistency question of which exceptional Jordan object is physically relevant. If the correct count of independent gauge-invariant nonlocal observables in the theory is 12, then J3(O) is the natural level. If the count exceeds 12, then J3(C⊗O) or a larger object may be needed.

This reframes the bridge question as a consistency question about the observable algebra: it is no longer only a choice between mathematical objects but a question with a determinate answer in principle.

---

## Interfaces to other domains

### From statics

- subgroup and representation structure to be checked for algebraic coherence
- candidate hypercharge construction
- generation organizer candidates

### From dynamics

- reduced generator to be checked for positivity and stability

### To interpretation

- clarifies which attractive stories are truly forced and which are not

### To phenomenology

- only a consistent framework is worth confronting with data

### To papers

- this domain determines which strong claims are publication-safe and which must be demoted

---

## Major unresolved issues

The consistency domain still owes:

1. a cleaner proof architecture for hypercharge uniqueness
2. a cleaner proof architecture for generation counting
3. a more precise distinction between geometric derivation and consistency completion
4. a clearer statement of which framework choices are canonical and which are contingent
5. a careful statement of the exact assumptions under which reduced-dynamics positivity is guaranteed

---

## Working bottom line

The consistency spine of the project is already useful.

At its safest level, it says:

1. the reduced dynamics can be consistent in the Markov regime
2. anomaly cancellation imposes real constraints on matter content
3. hypercharge and generation claims are partly constrained but not yet all equally proven
4. the strongest uniqueness and exclusion statements still carry substantial proof burden

This file should therefore be treated as the place where attractive claims are pressure-tested before they appear in papers.
