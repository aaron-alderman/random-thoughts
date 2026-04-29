# DIII Boundary Anomaly vs Matter-Content Constraints

## Purpose

This note advances the roadmap item:

- compare the DIII boundary anomaly data with the matter-content anomaly constraints.

The main outcome is a clarification of scope. The comparison is real, but the strongest possible phrasing is too strong in its current form.

---

## Starting point

Two statements are already live elsewhere in the corpus:

1. the corrected `Spin(2,3)` topological reading gives a DIII-type bulk/boundary story with unit winding magnitude `|W_3| = 1`, so the `m = 0` transition surface carries a protected massless `T1` boundary mode and a corresponding `T_0` / parity-type anomaly;
2. the static-consistency side treats `T1 \otimes (3 \oplus 1)` as the left-handed matter seed and uses anomaly cancellation to constrain what additional right-handed states are required.

The tempting bridge claim is:

> the DIII inflow condition and the matter-content anomaly cancellation are literally the same constraint.

This note checks how far that can safely be pushed.

---

## The 4d matter-content anomaly constraints

Take one Standard-Model-shaped generation written in the usual left/right language:

- `Q_L : (3,2)_{y_Q}`
- `L_L : (1,2)_{y_L}`
- `u_R : (3,1)_{y_u}`
- `d_R : (3,1)_{y_d}`
- `e_R : (1,1)_{y_e}`
- optional `nu_R : (1,1)_{y_nu}`

Then the familiar four-dimensional anomaly-cancellation conditions are:

$$
A_{SU(3)^2U(1)} = 2y_Q - y_u - y_d = 0,
$$
$$
A_{SU(2)^2U(1)} = 3y_Q + y_L = 0,
$$
$$
A_{\mathrm{grav}^2U(1)} = 6y_Q - 3y_u - 3y_d + 2y_L - y_e - y_{nu} = 0,
$$
$$
A_{U(1)^3} = 6y_Q^3 - 3y_u^3 - 3y_d^3 + 2y_L^3 - y_e^3 - y_{nu}^3 = 0.
$$

There is also the mod-2 `SU(2)` global condition:

- the number of left-handed `SU(2)` doublets must be even.

These constraints are the ones that tell the consistency layer which right-handed completion is allowed once the left-handed `T1` seed is chosen.

Two structural features matter here:

- the perturbative gauge anomalies depend on linear and cubic hypercharge data;
- the `SU(2)` global obstruction is mod 2.

---

## The 3d DIII boundary anomaly data

On the topological side, the `m = 0` transition surface is being read as the effective boundary of a DIII bulk. The relevant anomaly is the inability to regularize the boundary while keeping the protecting symmetry and gauge invariance manifest at the same time.

For a `2+1`-dimensional boundary fermion system, the induced parity-anomaly data is encoded by Chern-Simons counterterms. Up to convention-dependent normalizations, the gauge pieces are controlled by quadratic indices:

$$
\Delta k_G \propto \frac12 \sum_i T(R_i),
$$
$$
\Delta k_{U(1)} \propto \frac12 \sum_i q_i^2,
$$

with an analogous gravitational piece controlled by the net boundary fermion content. The DIII bulk inflow cancels this boundary obstruction.

Three points are crucial:

1. the boundary coefficients are quadratic in charges and representation indices;
2. the DIII invariant fixes a unit of protected boundary anomaly data, with sign/orientation tied to the chosen convention for `W_3`;
3. this data lives naturally on a `2+1`-dimensional boundary/transition surface, not directly in the `3+1`-dimensional perturbative anomaly polynomial.

---

## Direct comparison

The comparison is informative, but it does **not** support the literal statement that the two analyses are already "the same constraint."

### What does not match directly

The perturbative four-dimensional anomaly constraints and the three-dimensional parity anomaly do not use the same invariants:

- `SU(3)^2U(1)`, `SU(2)^2U(1)`, and `U(1)^3` anomalies are linear/cubic in hypercharge;
- the parity anomaly is quadratic in the boundary charges and Dynkin indices.

So a bare coefficient match of the form

> DIII inflow coefficient = full 4d gauge-anomaly coefficient

is too strong as written. They are different anomaly polynomials in different dimensions.

### What can match

There is still a meaningful lower-dimensional shadow:

1. the `SU(2)` mod-2 condition is the clearest common remnant.
   The `T1` matter seed gives `3 + 1 = 4` weak doublets per generation, which is even. That is exactly the kind of datum that survives both as the four-dimensional Witten condition and as the boundary parity/global obstruction.

2. the boundary parity anomaly can constrain the reduced transition-surface spectrum.
   If one dimensionally reduces the candidate `T1` matter content to the `m = 0` surface, then the sums of quadratic indices must be compatible with the DIII inflow supplied by the bulk.

3. the DIII story can therefore control a parity/global shadow of the matter content.
   What it does not yet do is replace the full perturbative `SU(3)^2U(1)`, `SU(2)^2U(1)`, `U(1)^3`, and mixed gravitational-`U(1)` cancellation problem.

---

## What the bridge should now mean

The safe reformulation is:

> DIII inflow may encode the `2+1`-dimensional parity/global shadow of the `T1` matter-content constraints after reduction to the transition surface.

That is a real and potentially valuable bridge. It would mean:

- the topological side checks whether the reduced `T1` boundary spectrum is globally/parity consistent;
- the consistency side checks whether the four-dimensional hypercharge completion is perturbatively anomaly free;
- a successful bridge would show that these are compatible reductions of one common matter sector, not that one calculation simply replaces the other.

---

## Refined next calculation

The right next step is no longer "match one coefficient and declare success."

It is:

1. specify the reduced `T1` boundary spectrum at the `m = 0` transition surface;
2. compute its `2+1`-dimensional parity-anomaly data for `SU(2)`, the selected `U(1)`, and any retained color sector;
3. isolate the mod-2/global piece and compare it with the four-dimensional weak-doublet counting condition;
4. only after that ask whether the quadratic boundary data can be obtained from a controlled reduction of the higher-dimensional anomaly polynomial.

That would turn the bridge from a slogan into a finite calculation.

---

## Minimal boundary-spectrum bookkeeping

One can already push the reduced bookkeeping a little further if one makes the minimal localization assumption:

> at the `m = 0` transition surface, the protected boundary matter inherited from the static side is the left-handed seed `Q_L \oplus L_L` coming from `T1 \otimes (3 \oplus 1)`.

This is only a working assumption. It is not yet derived that the full static matter seed localizes on the DIII transition surface in this way. But under this assumption, the parity/global bookkeeping is explicit.

### Weak/global piece

Per generation, the reduced boundary seed contains:

- one quark doublet `Q_L : (3,2)`
- one lepton doublet `L_L : (1,2)`

So the number of `SU(2)` doublets is

$$
N_{\mathrm{dbl}} = 3 + 1 = 4,
$$

which is even. This matches the four-dimensional mod-2 `SU(2)` consistency condition.

For the perturbative `2+1`-dimensional parity bookkeeping, the induced weak Chern-Simons level shift is proportional to

$$
\Delta k_{SU(2)} = \frac12 \sum_i T_2(R_i),
$$

with color multiplicity counted explicitly. Since `T_2(\mathbf 2)=1/2`,

$$
\sum_i T_2(R_i) = 3 \cdot \frac12 + 1 \cdot \frac12 = 2,
$$
$$
\Delta k_{SU(2)} = 1.
$$

So the weak-sector parity shift is integral. In other words:

- the global/mod-2 obstruction vanishes;
- the perturbative weak parity shift is not half-integral.

This is the cleanest point of contact between the DIII boundary story and the matter-content constraints.

### Color piece

For the same left-handed seed, the color contribution is

$$
\Delta k_{SU(3)} = \frac12 \sum_i T_3(R_i).
$$

Only the quark doublet contributes, with weak multiplicity `2`. Since `T_3(\mathbf 3)=1/2`,

$$
\sum_i T_3(R_i) = 2 \cdot \frac12 = 1,
$$
$$
\Delta k_{SU(3)} = \frac12.
$$

That is half-integral rather than integral. So if one literally localizes only the left-handed `T1` seed on the transition surface, the color parity bookkeeping is nontrivial and would require either:

- additional boundary states,
- an inflow term carrying the corresponding color response,
- or a weaker reading in which the DIII boundary mode is not the full `Q_L \oplus L_L` matter seed.

### `U(1)` piece

The `U(1)` part is normalization-dependent, so the safest statement is symbolic:

$$
\Delta k_{U(1)} = \frac12 \left( 6y_Q^2 + 2y_L^2 \right)
$$

for the left-handed seed alone.

If one uses the Standard-Model target values only as an illustrative check,

$$
y_Q = \frac16, \qquad y_L = -\frac12,
$$

then

$$
\Delta k_{U(1)} = \frac12 \left( 6 \cdot \frac{1}{36} + 2 \cdot \frac14 \right)
= \frac12 \left( \frac16 + \frac12 \right)
= \frac13.
$$

So in the illustrative Standard-Model normalization, the `U(1)` parity shift is again nontrivial.

### What this already tells us

The reduced bookkeeping now separates into two qualitatively different pieces:

1. the weak/global piece lines up neatly with the even-doublet consistency condition;
2. the color and `U(1)` parity data do not collapse to that same simple statement.

So the comparison has become sharper:

- the DIII bridge is already credible for the weak/global shadow;
- it is not yet credible as a full one-to-one identification of the entire gauge-anomaly system.

There is also a counting tension with the topological side. Even under the sharpened reading, the DIII discussion in `kernels/topological.md` concerns **one protected massless T1 channel in the minimal reduced block** at the transition surface. By contrast, the literal left-handed `T1` matter seed already contains, per generation,

- three quark-doublet copies, and
- one lepton-doublet copy.

So if the boundary story were read particle-by-particle, the static seed would look like a multi-multiplet boundary spectrum, not like a single protected mode. This strongly suggests that at least one of the following must be true:

1. the DIII boundary mode is a collective reduced channel rather than the full localized matter seed;
2. only a proper subchannel of the static `T1` matter seed is topologically protected at the transition;
3. additional degeneracy, flavor, or localization structure still has to be specified before the topological and static counts can be compared directly.

### Minimal-block reading already suggested by the corpus

The existing corpus already points to the most conservative reading of that counting tension.

On the topological side, the DIII calculation in `papers/paper2-diii-winding-number/` is performed on the reduced chiral Hamiltonian built from the bare `Spin(2,3)` gamma-matrix block. Its direct input is the four-component spinor alone.

On the static/reduction side, the corpus already says that this four-component block decomposes as

$$
\mathbf{4} = (\mathbf{2},-1/2)\oplus(\mathbf{2},+1/2)=T1\oplus T2,
$$

so the visible weak-doublet multiplicity is already part of the minimal topological block. By contrast, the color and generation structures are introduced elsewhere:

- color through the `(\mathbf 3 \oplus \mathbf 1)` factor in the static matter ansatz;
- generation through `J_3(O)` or the higher `2/4/6` access-ladder discussion.

So the safest current interpretation is:

> `W_3 = 1` is first a statement about one protected reduced `T1` channel in the minimal `Spin(2,3)` block, not yet a statement about the full color-and-generation-dressed matter spectrum.

This weakens the apparent contradiction substantially. The current topological result is prior to tensoring in any extra spectator structure.

### Spectator-copy consequence

If the extra internal sectors enter only as uncoupled spectators, then the total Hamiltonian takes the block form

$$
H_{\mathrm{tot}} = H_{\mathrm{Spin}(2,3)} \otimes I_{\mathrm{int}},
$$

and all additive topological/parity data scale with the number of uncoupled copies. In particular, one would expect:

- the total protected-mode count to multiply by the number of spectator copies;
- the parity-anomaly coefficients to add copy by copy.

But the current DIII paper computes only the invariant of the minimal block `H_{\mathrm{Spin}(2,3)}`. It does **not** yet specify whether color, generation, or right-handed completion appear as:

1. spectator tensor factors;
2. boundary-localized degrees of freedom inside the same protected channel;
3. bulk-only or non-topological sectors not counted by the minimal DIII invariant.

So the remaining question is not simply "why does one not equal many?" It is sharper:

> which parts of the static matter structure are actually present in the boundary Hamiltonian whose DIII invariant was computed?

### Scenario matrix

The localization problem can now be stated as a short list of explicit Hamiltonian scenarios.

#### Scenario A: minimal reduced block only

$$
H_{\partial} = H_{\mathrm{Spin}(2,3)}.
$$

Implications:

- the computed claim `|W_3| = 1` is the whole topological statement;
- the protected object is one reduced `T1` channel in the bare four-component block;
- color, generation, and right-handed completion are not yet part of the boundary Hamiltonian.

This is the most conservative reading, and it is fully compatible with the current DIII paper.

#### Scenario B: uncoupled spectator copies

$$
H_{\partial} = H_{\mathrm{Spin}(2,3)} \otimes I_{N_{\mathrm{spec}}}.
$$

Implications:

- the protected-mode count multiplies by `N_{\mathrm{spec}}`;
- additive parity data also multiply by `N_{\mathrm{spec}}`;
- if `W_3(H_{\mathrm{Spin}(2,3)}) = \pm 1`, then the total invariant is expected to be
  $$
  W_3(H_{\partial}) = N_{\mathrm{spec}}\,W_3(H_{\mathrm{Spin}(2,3)}).
  $$

So if the full boundary Hamiltonian literally carried, for example, one independent copy for each color/lepton slot, then one would expect a multiple of the minimal invariant rather than the bare unit result. This means Scenario B is not the current calculated statement; it is a possible extension of it.

#### Scenario C: full left-handed `T1` matter seed localized on the boundary

Here one takes the boundary spectrum to contain the whole `Q_L \oplus L_L` seed.

Implications:

- the weak/global `SU(2)` shadow works cleanly;
- the color and illustrative `U(1)` parity data are nontrivial, as computed above;
- the protected-channel count no longer looks minimal unless the localized seed is further organized into collective channels.

So Scenario C requires additional structure beyond the present topological computation.

#### Scenario D: only a reduced protected subchannel localizes

Here the DIII invariant protects one collective channel, while the rest of the static matter structure is:

- bulk-only,
- non-topological,
- or localized but not symmetry-protected by the same minimal invariant.

This is currently the best candidate if one wants to keep:

- the exact minimal-block `|W_3| = 1` result,
- the weak/global `SU(2)` shadow,
- and the possibility of richer color/generation structure elsewhere in the framework.

### Immediate consequence

Scenarios A and D are compatible with the present state of the corpus without further topological input.

Scenarios B and C are not ruled out, but they are not what has been computed. They would require a new Hamiltonian-level extension in which the spectator or matter sectors are explicitly included in the boundary operator before any `W_3` or inflow claim is upgraded.

### Corpus default and upgrade rule

For the current corpus, the clean default reading should now be fixed explicitly:

- **established reading:** Scenario A;
- **working extension for the anomaly bridge:** Scenario D;
- **upgrade-required alternatives:** Scenarios B and C.

This means:

1. whenever the repo cites the present DIII calculation as an established result, it should be read in Scenario A form:
   one protected reduced `T1` channel in the minimal four-component `Spin(2,3)` block;
2. whenever the repo speculates about connecting that topological statement to richer matter structure, the safe working hypothesis is Scenario D:
   one protected reduced channel plus additional static structure that is not yet proved to sit in the same protected boundary Hamiltonian;
3. any attempt to promote spectator multiplication or full `Q_L \oplus L_L` localization into the live topological claim must first write down the enlarged boundary Hamiltonian and recompute `W_3` and the induced parity data there.

So the practical rule is simple:

> until a larger boundary Hamiltonian is explicitly built and analyzed, the topological corpus should speak in Scenario A language and treat Scenario D as the leading bridge hypothesis.

This suggests that the next calculation must answer a localization question before it can answer a matching question:

> does the DIII boundary mode represent the whole static `T1` matter seed, or only a reduced protected channel inside it?

Until that is fixed, any stronger anomaly-inflow identification remains underdetermined.

---

## Bottom line

The DIII/topological comparison is still worth pursuing, but it sharpens the project in a more disciplined way than the strongest bridge claim suggested.

- The strongest current statement is too strong: the DIII inflow condition is not literally identical to the full four-dimensional matter-content anomaly constraints.
- The promising weaker statement survives: DIII inflow may capture a lower-dimensional parity/global shadow of those constraints, especially the even-doublet obstruction.
- The next useful task is therefore a reduced boundary-spectrum calculation, not a direct identification of the entire gauge-anomaly system with the DIII inflow coefficient.
