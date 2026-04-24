# Ambient-to-Observable Reduction Scaffold

## Purpose

This note turns the project's largest missing-middle problem into a concrete work surface.

The framework already has:

- a plausible parent anchor in the octonionic branch
- a reduced effective branch organized by `Spin(2,3)`
- several local phenomenological and topological results inside that reduced branch

What it still lacks is a disciplined account of how one passes from the parent structure to the reduced and observable structure without smuggling in the answer by hand.

This note is therefore not a finished derivation. It is a scaffold for the derivation.

---

## The three-step path

The highest-value current path is:

1. Parent-to-effective reduction
2. Bulk-to-transport dynamical derivation
3. Observable bridge

These are not separate projects. They are one chain.

### Step 1. Parent-to-effective reduction

Define the map from the parent octonionic geometry to the effective `Spin(2,3)` branch.

This is the current note.

### Step 2. Bulk-to-transport dynamical derivation

Once the effective branch variables are identified cleanly, derive the two-branch equations from a bulk action, moment map, or equivalent Hamiltonian structure.

### Step 3. Observable bridge

Once the reduced variables and dynamics are controlled, identify which quantities correspond to observables, invariants, and possible phenomenological signatures.

---

## The bridge object

The object the project owes can be stated cleanly:

> a reduction map from ambient octonionic structure to the effective `Spin(2,3)` transport branch and then to the observable sector

At minimum, the reduction has to explain:

1. why the selected octonionic direction is physically privileged
2. how the hidden remainder `u^\perp \cong \mathbf{C}^3` is organized
3. how a local quaternionic `H` slice carries the hidden complex-plane data
4. how the exploratory `Spin(3,3)` lift folds into that hidden complex-plane structure
5. how the effective `T1/T2` split and `J^{01}` grading emerge from that folded data
6. what ambient, dynamical, or epistemic selector induces the final observable projector, conventionally named `T1` after orientation is fixed

If those six points are not addressed, the project still lacks its missing middle.

---

## Provisional reduction chain

The present best candidate chain is:

$$
\mathbb{O}
\supset
\mathbf{R}u \oplus u^\perp
\cong
\mathbf{R}u \oplus \mathbf{C}^3
\supset
H_{\mathrm{loc}}
\rightsquigarrow
\text{hidden complex plane}
\rightsquigarrow
\text{effective two-sector branch}
\rightsquigarrow
\mathrm{Spin}(2,3)
\rightsquigarrow
(T1,T2)
\rightsquigarrow
\text{observable } T1 \text{ channel}.
$$

This chain should be read carefully.

- `\mathbf{R}u \oplus u^\perp` is parent geometry
- `u^\perp \cong \mathbf{C}^3` is the hidden remainder
- `H_{\mathrm{loc}}` is not the whole parent remainder, but the local carrier of the hidden complex-plane data relevant to the reduced branch
- the effective two-sector branch is what remains after the hidden plane structure is folded into a `Spin(2,3)` description

The weak point at present is the arrow labeled "folded into a `Spin(2,3)` description". That arrow is where the project most needs explicit mathematics.

---

## Safe claims and active conjectures

### Safe claims

- fixing an imaginary octonionic direction reduces `G2` to `SU(3)`
- the hidden remainder is naturally `u^\perp \cong \mathbf{C}^3`
- a two-sector effective branch exists in the `Spin(2,3)` kernel
- the current `T1/T2` split is best read as an effective reduced image, not as the final parent ontology

### Active conjectures

- the relevant hidden complex-plane data is carried locally by a quaternionic `H` slice inside `u^\perp`
- the exploratory `Spin(3,3)` structure should be read as over-complete bookkeeping for that hidden plane data
- the `J^{01}` grading is the reduced image of this folded hidden structure
- the observable `T1` channel is selected by the same direction choice that fixes the zero-mass traversal channel

These conjectures are central, but they are not yet theorems.

---

## Working reduction kernel

This is the short version of the scaffold that the rest of the project can cite without importing every exploratory step.

### Inputs

1. Fix a preferred imaginary octonionic direction `u` with `u^2 = -1`.
2. Use the resulting complex remainder
   $$
   u^\perp \cong \mathbf{C}^3
   $$
   as the hidden parent sector.
3. Choose a local unit `v \in u^\perp` and form
   $$
   H(u,v) = \mathrm{span}_{\mathbf{R}}\{1,u,v,uv\},
   \qquad
   \Pi(u,v) = \mathrm{span}_{\mathbf{R}}\{v,uv\}.
   $$
4. Read `\Pi(u,v)` as the local hidden complex line and `J_u|_{\Pi}` as its phase generator.

### Reduced output

The reduced branch is required to keep only the phase-charge information of the hidden line and forget the internal frame data used to describe it.

At the current safe level, this means:

1. the effective spinor space decomposes as
   $$
   \mathcal{H}_{\mathrm{spin}} = T1 \oplus T2
   $$
   with `J^{01}` acting as the reduced grading generator
2. the `T1/T2` split is interpreted as the reduced opposite-charge image of the hidden phase split on `\Pi(u,v)`
3. the quaternionic slice is treated as local reduction geometry, not yet as a new physical interaction sector

### Minimal operator statement

If the parent hidden line admits charge projectors `P_{\Pi,-}` and `P_{\Pi,+}`, then the reduction should preserve support in the minimal sense

$$
\mathcal{R}_{\mathrm{op}}(P_{\Pi,-}) = P,
\qquad
\mathcal{R}_{\mathrm{op}}(P_{\Pi,+}) = Q,
$$

where `P` and `Q` project onto `T1` and `T2`.

At this stage the only acceptable sign ambiguity should be the global one coming from reversing the overall time orientation. Once the static convention

$$
J^{01}
= -\frac12
\begin{pmatrix}
\mathbf{1}_2 & 0 \\
0 & -\mathbf{1}_2
\end{pmatrix}
$$

is fixed, `T1` is by definition the `J^{01}` eigenspace of eigenvalue `-1/2` and `T2` is the eigenspace of eigenvalue `+1/2`. The parent-to-reduced sign dictionary should therefore be chosen so that `P_{\Pi,-}` maps to `T1` and `P_{\Pi,+}` maps to `T2`.

Then any parent zero-mass operator supported only on the `(-)` sector,

$$
H_{\Pi}^{(0)} = P_{\Pi,-} H_{\Pi}^{(0)} P_{\Pi,-},
$$

reduces to an operator satisfying

$$
H_0 = P H_0 P,
\qquad
QH_0 = H_0Q = 0.
$$

This is the cleanest current Route A bridge from the parent hidden line to the reduced zero-mass transport claim.

### Minimal parent zero-mass selection rule

The support assumption on the parent zero-mass operator can itself be decomposed into two smaller claims.

First, require **phase covariance** on the hidden line:

$$
[H_{\Pi}^{(0)},J_{\Pi}] = 0
\qquad\text{equivalently}\qquad
[H_{\Pi}^{(0)},K_{\Pi}] = 0.
$$

Because the complexified hidden line splits into the two one-dimensional charge sectors of `K_{\Pi}`, this already forces

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-} + h_+ P_{\Pi,+}
$$

for some scalars or reduced transport generators `h_\pm`. So phase covariance by itself rules out zero-mass mixing between the two hidden charge sectors.

Second, add the **one-sector traversal principle**:

- the same selected direction `u` that defines the privileged traversal channel also orients the hidden phase split
- direct zero-mass traversal uses only one of the two oriented charge sectors

Then the direct zero-mass target is

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-}
\qquad\text{or equivalently}\qquad
H_{\Pi}^{(0)} = P_{\Pi,-} H_{\Pi}^{(0)} P_{\Pi,-}.
$$

With the static `J^{01}` convention fixed, that sign choice can be made explicit: `P_{\Pi,-}` is the parent sector that maps to `T1`, and `P_{\Pi,+}` maps to `T2`.

This is a real improvement in the blocker structure. The project no longer needs to treat parent zero-mass support on one sector as a single opaque assumption. It can instead say:

1. phase covariance of the hidden line gives charge-diagonality
2. one-sector traversal is the remaining nontrivial selection principle

What is still not derived is the second step. The live question is why the chosen direction `u` should force one-sector traversal rather than allow both `h_-` and `h_+` to remain active.

### Minimal oriented-channel consistency argument

The remaining selection step can now be narrowed further by using the fact that `u` is meant to be an oriented physical choice, not just an unoriented axis.

Under reversal of the selected direction,

$$
u \mapsto -u,
$$

the hidden complex structure changes sign on the local plane:

$$
J_{\Pi} \mapsto -J_{\Pi},
\qquad
K_{\Pi} \mapsto -K_{\Pi},
$$

so the two hidden charge projectors are exchanged:

$$
P_{\Pi,-} \leftrightarrow P_{\Pi,+}.
$$

This means the two charge sectors should be read as the two opposite orientations of the same hidden line, not as two unrelated slots.

Now take the most general charge-diagonal parent zero-mass operator:

$$
H_{\Pi}^{(0)} = h_- P_{\Pi,-} + h_+ P_{\Pi,+}.
$$

There are then three qualitatively different cases.

1. If `h_- = h_+`, the direct zero-mass channel is blind to the orientation of `u`; the selected direction survives only as an unoriented axis.
2. If both `h_-` and `h_+` are nonzero and unequal, the theory has two direct oriented zero-mass channels on the same hidden line.
3. If exactly one coefficient is nonzero, the selected oriented direction defines one direct zero-mass channel.

The current framework already wants two further things:

- the selected direction `u` should remain physically meaningful after reduction
- the zero-mass readout channel should be unique rather than doubled

Under those two requirements, the third case is the minimal consistent realization. So one-sector traversal is no longer just an arbitrary extra preference. It is the minimal way for an oriented choice of `u` to survive as a unique direct channel in the reduced theory.

What this still does **not** prove is that the parent geometry by itself fixes the remaining global orientation convention. Once time orientation is fixed, the sign dictionary is fixed with it; the live issue is whether that global convention is geometrically forced or only fixed when one ties the reduction to the observable arrow of readout. But it does mean the remaining live issue is narrower:

- not whether one-sector traversal is pure taste
- but whether the framework's oriented-direction and unique-channel principles, together with a readout orientation choice, should be accepted as part of the reduction architecture

### Safe use of this kernel

The project may now safely say:

- the local quaternionic slice gives an explicit carrier of hidden complex-plane data
- the visible `T1/T2` split is the reduced image of hidden phase-charge structure, not an unexplained doubling
- the quaternionic sector is important bridge structure but is non-blocking if its final canonical status remains unresolved

### What this kernel does not yet prove

It does not yet prove:

- that the choice of `v` is canonical
- that the reduction map is uniquely fixed
- that the operator identities above have been fully derived rather than reduced to a sharp target
- that the full bulk transport equations have already been obtained

---

## Concrete subproblems

The reduction problem splits into four bounded tasks.

### R1. Quaternionic carrier

Show explicitly how a local quaternionic `H` slice sits inside the octonionic remainder and carries a distinguished complex plane.

Deliverable:

- a clean algebraic description of the embedding
- the exact sense in which the complex plane is local rather than global

#### R1. Working algebraic form

Fix a unit imaginary octonion `u` with `u^2 = -1`. Then the real orthogonal complement of `u` inside the imaginary octonions,

$$
u^\perp \subset \mathrm{Im}(\mathbb{O}),
$$

is `6`-dimensional. Left multiplication by `u` defines

$$
J_u(x) := ux.
$$

By alternativity,

$$
J_u^2(x) = u(ux) = (u^2)x = -x,
$$

so `J_u` is a complex-structure candidate on `u^\perp`. This is the clean algebraic reason one may write

$$
u^\perp \cong \mathbf{C}^3
$$

once `u` is chosen.

Now choose a unit vector `v \in u^\perp`. Since any two octonions generate an associative subalgebra, the real span

$$
H(u,v) := \mathrm{span}_{\mathbf{R}}\{1, u, v, uv\}
$$

is a quaternionic subalgebra of `\mathbb{O}`.

This gives the first explicit candidate for the local quaternionic carrier:

$$
H_{\mathrm{loc}} = H(u,v).
$$

Inside that quaternionic slice, the part lying in the hidden remainder is

$$
\Pi(u,v) := H(u,v) \cap u^\perp = \mathrm{span}_{\mathbf{R}}\{v, uv\}.
$$

This is a real `2`-plane in `u^\perp`, and it is `J_u`-invariant because

$$
J_u(v) = uv, \qquad J_u(uv) = u(uv) = -v.
$$

So `\Pi(u,v)` is naturally a complex line inside `u^\perp \cong \mathbf{C}^3`.

This is the present best candidate for the hidden complex plane carried by a local quaternionic slice.

#### Why this is local, not yet global

The construction above depends on the extra choice of `v`.

- choosing `u` alone gives the full `6`-dimensional remainder `u^\perp`
- choosing `v` inside `u^\perp` picks one complex line `\Pi(u,v)` inside that remainder
- different choices of `v` produce different quaternionic slices `H(u,v)`

So the construction is local in exactly this sense:

- the parent branch supplies the ambient complex `3`-space
- the quaternionic slice supplies one distinguished complex line within it
- but the framework does not yet know which `v` is canonically selected, or whether that selection is dynamical, kinematical, or epistemic

That unresolved selection problem is why the current claim should remain:

- explicit local carrier: available
- canonical global carrier: not yet derived

### R2. Folding map

Formalize the map by which the exploratory `Spin(3,3)` lift reduces to hidden complex-plane data instead of literal extra timelike structure.

Deliverable:

- a map of variables or generators
- a statement of what survives and what is gauge or redundancy

#### R2. Minimal structural requirements

Even before a full generator-level derivation is available, the fold map can be constrained by what it must accomplish.

The exploratory `Spin(3,3)` lift should no longer be read as the final ontology. Its value is that it exposed a doubled or two-plane structure that must now be re-read as hidden complex-plane data.

So the fold map should have the following schematic form:

$$
\mathcal{F} :
\{\text{lifted two-plane data}\}
\longrightarrow
\{\Pi(u,v),\; J_u|_{\Pi},\; J^{01},\; T1 \oplus T2\}.
$$

In words:

- the lift begins with a doubled internal two-plane structure
- the fold keeps only the part that survives as hidden complex-plane data in the local quaternionic slice
- the remainder is reduced to the effective grading and sector split seen in the `Spin(2,3)` branch

#### What should survive the fold

The reduced image should at least retain:

1. a distinguished complex line `\Pi(u,v)` inside `u^\perp`
2. the induced complex structure `J_u|_{\Pi}`
3. a residual grading or charge that becomes the effective `J^{01}` split
4. a two-sector decomposition that is visible as `T1 \oplus T2`

#### What should be quotiented away

The fold should remove data that only records how the hidden plane is framed, rather than which hidden plane is physically selected.

At the schematic level, this means:

- frame changes internal to the lifted two-plane should not survive as literal extra timelike directions
- only the induced complex structure and its reduced grading effect should remain visible
- the lift should therefore be read modulo internal frame redundancy

This is the core re-interpretation:

- not "two extra times survive"
- but "a hidden oriented complex plane leaves behind a reduced two-sector image"

#### Provisional local picture

The most conservative local candidate is:

- the lifted object encodes a two-plane with orientation and internal phase data
- the fold identifies that two-plane with the complex line `\Pi(u,v) \subset u^\perp`
- the residual action of rotating the hidden plane becomes the effective `U(1)` grading seen as `J^{01}`
- the two eigensectors of that reduced grading are the visible `T1` and `T2` sectors

This should still be treated as a programme statement, not a theorem. But it is sharp enough to guide the next derivation attempt.

### R3. Reduced grading

Show how the effective two-sector branch and `J^{01}` grading arise from the folded hidden structure.

Deliverable:

- an explicit reduced decomposition
- a statement of what information is lost in the reduction

#### R3. Working reduced decomposition

The most conservative reduced picture is to retain from the hidden complex line only its phase-rotation symmetry.

Once `\Pi(u,v)` is identified as a complex line, it carries a natural unitary phase action

$$
z \mapsto e^{i\alpha} z,
$$

with generator `U(1)_{\Pi}`.

The proposal is that the effective `Spin(2,3)` grading remembers this hidden phase action only through its lifted charge decomposition on the reduced spinor space.

So, instead of keeping the full parent data of the quaternionic slice, the reduction keeps only a two-charge splitting:

$$
\mathcal{H}_{\mathrm{red}} = W_{-1/2} \oplus W_{+1/2},
$$

where each `W_{\pm 1/2}` is a real two-dimensional block, or equivalently a complex one-dimensional weight space together with the visible `SU(2)` doublet structure carried by the `Spin(2,3)` branch.

At this level, the effective generator is

$$
J^{01}_{\mathrm{eff}}
=
\begin{pmatrix}
-\tfrac12\,\mathbf{1}_2 & 0 \\
0 & +\tfrac12\,\mathbf{1}_2
\end{pmatrix},
$$

up to the project sign convention already used in `kernels/statics.md`.

This gives the reduced identification

$$
T1 = W_{-1/2}, \qquad T2 = W_{+1/2}.
$$

The point is not that the hidden complex line literally is `J^{01}`. The point is that, after folding and reduction, the only surviving imprint of that hidden line is an effective `U(1)` charge splitting, and this is exactly the role `J^{01}` plays in the reduced `Spin(2,3)` description.

#### What the reduction forgets

This reduced decomposition is intentionally lossy. It forgets:

- which vector `v` inside `u^\perp` was chosen to define the local quaternionic slice
- how the complex line `\Pi(u,v)` sits inside the full `\mathbf{C}^3` remainder
- the frame data internal to the lifted two-plane
- any parent information that does not survive as the effective `U(1)` grading and the two-sector split

So `T1 \oplus T2` should be read as the reduced charge image of the hidden plane, not as a faithful copy of the full parent geometry.

#### Why this is the right level of claim

This proposal matches several things already present in the kernel:

- `J^{01}` is the generator of the `U(1)` factor in the maximal compact subgroup
- the spinor decomposes into two blocks of opposite `J^{01}` charge
- the folded reading of the framework wants the split to arise from hidden complex-plane data rather than from literal surviving extra time directions

What is still missing is the full derivation that takes a parent action of the hidden plane and proves that its reduced image is exactly the explicit `J^{01}` matrix in the chosen `Spin(2,3)` representation.

So the safe status is:

- reduced grading picture: structurally plausible and now explicit
- full derivation of the grading map: still open

### R4. Observable selection

Explain what selects the final observable projector, rather than treating the block name `T1` as intrinsically preferred.

Deliverable:

- either a dynamical selection argument
- or a principled epistemic postulate stated sharply enough that it can be tracked as an assumption

#### Regime split (massless vs massive)

One source of confusion is that the framework uses `Spin(2,3)` both as a reduced transport symmetry and as a convenient bookkeeping arena for the two-sector split. These roles should be separated by regime.

**Massless (direct readout / null transport) regime.** The natural kinematic arena is Lorentz/conformal (`Spin(1,3)` or the ambient `SO(2,4)` layer). In this regime the observable rule should be stated as a *support* or *boundary/readout* principle (the massless channel has support only on the selected sector), with the remaining global `\mathbf{Z}_2` fixed by the chosen forward/readout orientation. One should not demand that `Spin(2,3)` by itself "prefers" the block called `T1` in the massless limit.

**Massive (mixing) regime.** Once there is genuine mixing between the two reduced sectors (off-diagonal `T1/T2` operators, mass terms, excursions), `Spin(2,3)` becomes a relevant effective symmetry of the reduced dynamics. In this regime it is appropriate to use the `J^{01}` grading and associated operators as part of the transport kernel.

**Where the axis data lives.** The reason one cannot "act lower" to derive the selector inside the reduced slice is that the local geometry is already adapted to upstream selection data. The choice of octonionic direction `u` (and its stabilizer) is the parent datum that breaks the transverse symmetry; the reduced basis and any induced local axis representative `\hat a` are downstream gauge-fixes of that datum, not additional physical choices made inside `Spin(2,3)`.

#### Scale-flow selector caveat

There is a sharper way to state the live issue.

The label `T1` is not itself expected to be intrinsically preferred. It is a reduced-sector name fixed only after an orientation convention has been supplied. The invariant object should be the sector selected by the ambient readout or scale-flow direction, with `T1` used as the name of that sector once the reduced basis has been oriented.

In that reading, the question is not:

- why does `Spin(2,3)` internally prefer the block called `T1`?

but rather:

- what ambient scale-flow or readout vector induces the reduced projector onto the observable sector?
- does the induced projector agree with the `J^{01}` eigenspace convention currently called `T1`?

This matters because `Spin(2,3)` is naturally tied to the reduced `AdS_4`/`SO(2,3)` geometry. If the selector lives instead in a larger scale or conformal geometry, for example an `AdS_5`/`SO(2,4)`-type ambient layer, then the selection principle belongs one level above the reduced `Spin(2,3)` branch. In that case the scaffold should not try to prove that `T1` is special from `Spin(2,3)` alone. It should try to prove the descent diagram:

$$
\text{ambient scale/readout flow}
\longrightarrow
\text{reduced } Spin(2,3) \text{ slice}
\longrightarrow
J^{01}\text{ two-sector split}
\longrightarrow
\text{observable projector}.
$$

Under this convention, `T1` means "the reduced sector aligned with the induced forward/readout flow." The name is conventional; the induced projector is the object that would have invariant content.

#### Minimal ambient-selector test

The simplest way to make the previous caveat operational is to introduce an ambient selector object

$$
D_{\mathrm{amb}} \in \mathfrak{so}(2,4)
$$

or an equivalent ambient scale-flow vector field whose infinitesimal action is represented by such a generator.

Let the reduced `Spin(2,3)` slice be obtained by fixing the spacelike normal `n`, so that at the vector level

$$
V_{2,3} = n^\perp \subset V_{2,4}.
$$

Then the selector test is:

1. restrict or project `D_{\mathrm{amb}}` to the slice-preserving component
   $$
   D_{\mathrm{red}} := \operatorname{pr}_{\mathfrak{so}(2,3)}(D_{\mathrm{amb}});
   $$
2. check whether `D_{\mathrm{red}}` is conjugate, with orientation, to the reduced compact charge generator `J^{01}`;
3. define the observable projector as the negative-charge or positive-charge spectral projector of `D_{\mathrm{red}}`, according to the forward orientation selected by the ambient flow;
4. name that sector `T1`.

In this formulation, the sign is the only real convention. If

$$
D_{\mathrm{red}} = J^{01},
$$

then the current naming is retained. If

$$
D_{\mathrm{red}} = -J^{01},
$$

then the labels `T1` and `T2` should be swapped. No physical content changes, because the invariant content is the induced projector

$$
P_{\mathrm{obs}}
=
\chi_{\mathrm{forward}}(D_{\mathrm{red}}),
$$

not the bare sector name.

This turns the `AdS_5` / `SO(2,4)` suspicion into a finite check rather than a new philosophical burden:

- identify the ambient scale-flow generator;
- restrict it to the `SO(2,3)` slice fixed by `n`;
- compare the result with `J^{01}`;
- use the resulting spectral projector as the observable projector.

A minimal vector-representation sanity check for this projection test lives at `checks/check_so24_selector.py`.

**Collapse lemma (why this is "relatively simple").**
If the induced selector is required to pick no preferred spatial axis in the reduced slice, then it should commute with the spatial rotation algebra
$$
\mathfrak{so}(3)=\mathrm{span}\{J^{23},J^{34},J^{42}\}\subset \mathfrak{so}(2,3).
$$
In that case, representation-theoretically the only remaining nontrivial slice-preserving generator is the compact `\mathfrak{so}(2)` in the `(0,1)` plane, hence
$$
D_{\mathrm{red}} \propto J^{01}.
$$
So any two "null/time/scale/readout" selectors that satisfy:
1) slice preservation, and
2) no preferred spatial axis,
must collapse to the same induced observable projector up to the global sign `D_{\mathrm{red}}=\pm J^{01}`. The only remaining data is the orientation choice (which sign is forward), i.e. the same `\mathbf{Z}_2` already isolated elsewhere in this scaffold.

This lemma is a *specialization*, not a default assumption. It is the correct endpoint only if the framework truly insists that the selector cannot encode any local axis data downstream of the parent reduction. If instead the selector is allowed to carry (or induce) a local axis, then the axis-level `SO(2,1)` story should be kept alive rather than collapsed away, because it is precisely the regime where threshold phenomena can live.

**Local-axis variant (more modest claim).**
If instead the selector is allowed to pick a *local* spatial axis, then one should only require commutation with the `SO(2)` stabilizer of that axis. For example, choosing axis `4` means preserving rotations in the `(2,3)` plane, generated by `J^{23}`.

In that case the induced selector is no longer forced to be proportional to `J^{01}`. The natural surviving family is the `\mathfrak{so}(2,1)` subalgebra acting on the three-index block `(0,1,\hat a)`:
$$
\mathfrak{so}(2,1)_{\hat a}=\mathrm{span}\{J^{01},J^{0\hat a},J^{1\hat a}\},
\qquad
\hat a\in\{2,3,4\}.
$$
This is exactly the situation where "null/time/scale" and "a local spatial axis" are linked: the selector can now mix the time plane with the chosen spatial axis while leaving the transverse plane invariant.

Inside a fixed axis block `\mathfrak{so}(2,1)_{\hat a}`, there are three standard conjugacy types for a nonzero generator (elliptic/compact, hyperbolic/boost, and parabolic/null). The sanity checker reports simple invariants of the induced `3\times 3` axis block (for example `\mathrm{tr}(M^2)`): with axis `4`, one finds `J^{01}` is elliptic (`\mathrm{tr}(M^2)<0`), `J^{04}` is hyperbolic (`\mathrm{tr}(M^2)>0`), and `J^{01}+J^{04}` is parabolic (`\mathrm{tr}(M^2)=0`). This matters because the observable-selection step above was phrased as a *spectral projector* of `D_{\mathrm{red}}`. That language is natural when the induced selector is diagonalizable and gapped (elliptic). If the induced selector is parabolic (a "null" generator), then the framework must replace the projector language by a filtration or limiting prescription.

Once a diagonalizable `D_{\mathrm{red}}` is fixed, the dependence of the observable projector `P_{\mathrm{obs}}` on parameters and mixing is exactly the setting of `research/spectral-transition/`: projector variation is gap-amplified, and the local two-mode normal form captures how a small off-diagonal coupling can rotate a one-dimensional observable sector into its complement when the gap becomes small.

**Efimov remark.** This local-axis `SO(2,1)` sector is also the same threshold arena used in the Faddeev/Efimov bridge track (where a universal critical value separates non-oscillatory scaling from log-periodic/discrete-scale behavior). If that bridge is real, it is a reason *not* to collapse immediately to the axis-free `D_{\mathrm{red}}\propto J^{01}` case: the threshold transition lives precisely in the richer axis `SO(2,1)` family. See `research/faddeev-efimov/casimir-faddeev-conjecture.md` and `research/faddeev-efimov/derivations/3-eigenvalue-flow.md` for the corresponding "eigenvalue-flow" formulation.

In the octonionic reduction language, the "local axis" should not be read as an arbitrary choice of `\hat a`. It is the selected octonionic direction `u`, expressed in an adapted local quaternionic slice and then mapped into the reduced basis. By transitivity, one may gauge-fix that direction to a standard imaginary unit (for example `u = e1` in an octonion basis), and the corresponding reduced spatial index `\hat a` is then fixed only up to the same harmless relabeling already present in the visible Pauli-triplet dictionary.

Equivalently: within `Spin(2,3)` alone, the choice of `\hat a` is conjugate under the `SO(3)` rotations and is therefore "gauged away" unless a higher object breaks that symmetry. In this programme that higher object is the parent/octonionic selection data (the choice of `u`).

**Working convention.** Once `u` is fixed by the parent reduction, one may choose a reduced basis representative `\hat a` for calculations without claiming it is intrinsic. Concretely:
1) use `--axis any` when checking a candidate selector at the level of invariance class, and
2) after that, pick a convenient representative axis (for example `\hat a = 4`) to write explicit matrices in the chosen gamma basis.

The sanity checker `checks/check_so24_selector.py` supports this via `--axis any` (meaning "some axis up to `SO(3)` relabeling") and via `--axis 2|3|4` when one wants a concrete representative axis in the current reduced basis. It reports whether `D_{\mathrm{red}}` lies in the corresponding axis `\mathfrak{so}(2,1)` block.

#### R4. Two legitimate routes

At the present level of the project, `R4` should be split cleanly into two different routes.

### Route A. Dynamical selection

The stronger route would show that the observable channel is not chosen independently, but is forced by the interaction structure itself.

In this route, one would try to prove:

- the ambient readout or scale-flow direction descends to the same reduced orientation as the selected octonionic direction `u`
- zero-mass propagation couples directly only to one reduced charge sector
- that sector is the one named `T1` after the induced orientation is fixed
- `T2` enters only through massive mixing, hidden excursions, or off-diagonal corrections

If this route succeeds, then projection onto `T1` is not a primitive axiom. It is the observational shadow of a dynamical selection rule.

This is the strongest possible outcome, but it is not yet derived.

### Route B. Epistemic postulate

The weaker but still disciplined route is to state openly:

- the reduction yields a two-sector branch `T1 \oplus T2`
- one of those sectors is identified as the zero-mass readout channel
- the framework postulates that observable access follows the sector induced by the ambient readout or scale-flow orientation

In this route, the claim is not that the label `T1` has already been forced. The claim is that once the zero-mass interaction channel and forward readout orientation are chosen, the sector named `T1` is the correct effective observational sector.

This route is weaker, but still coherent and honest. It matches the current level of the epistemics file better than pretending the full dynamical selection has already been earned.

#### Present best status

The project currently sits between these two routes:

- stronger than a bare primitive projection axiom, because the observable channel is tied to the selected zero-mass interaction structure
- weaker than a full dynamical theorem, because the forcing argument that uniquely identifies `T1` has not yet been completed

So the clean current formulation is:

> the observable rule is an effective postulate downstream of a partially structured channel-selection story

That is the right level of honesty for the present framework.

#### What would close R4

`R4` would be in much better shape if the project could do either of the following:

1. derive that the ambient scale/readout flow induces a reduced projector agreeing with the `J^{01}` sector named `T1`
2. derive that zero-mass transport operators act only on that induced sector in the reduced branch
3. state a sharpened epistemic principle saying that observable access follows the selected zero-mass channel, with the naming of that channel as `T1` tracked explicitly as an orientation convention

Any of these would be progress. The first two are stronger. The third is already within reach and should be written clearly.

#### Minimal Route A target

The cleanest near-term version of Route A is not yet a full theorem. It is a disciplined operator target.

Write the reduced generator as

$$
H = H_0 + H_{\mathrm{mix}},
\qquad
H_0 =
\begin{pmatrix}
H_{\mathrm{tr}} & 0 \\
0 & 0
\end{pmatrix},
\qquad
H_{\mathrm{mix}} =
\begin{pmatrix}
0 & mV \\
mV^\dagger & H_2
\end{pmatrix}.
$$

Then the Route A derivation problem becomes:

- prove that the parent reduction forces the zero-mass transport operator into the `H_0` block
- prove that `H_0` acts only on the sector selected by the induced observable projector
- prove that `T2` enters only through `H_{\mathrm{mix}}`

The sharpest algebraic version of that target is:

$$
H_0 = P H_0 P,
\qquad
Q H_0 = 0,
\qquad
H_0 Q = 0,
\qquad
Q = 1-P,
$$

with `P` the induced observable projector, named `T1` after the readout orientation is fixed.

So the real Route A question is:

- can those identities be obtained from the parent reduction, the selected zero-mass channel, and, if needed, the ambient scale-flow selector

instead of merely being imposed as a convenient block ansatz?

#### Minimal parent-side candidate

The cleanest parent-side candidate currently available is to define the charge split first on the hidden complex line itself.

On the local plane `\Pi(u,v)`, the complex structure is

$$
J_{\Pi} := J_u|_{\Pi},
\qquad
J_{\Pi}^2 = -1.
$$

After complexification of `\Pi(u,v)`, define the phase-charge operator

$$
K_{\Pi} := i J_{\Pi},
$$

so that `K_{\Pi}` has eigenvalues `\pm 1` on the complexified line. Its spectral projectors are

$$
P_{\Pi,\pm} = \frac12(1 \pm iJ_{\Pi}),
$$

with `P_{\Pi,-}` the `K_{\Pi}=-1` projector and `P_{\Pi,+}` the `K_{\Pi}=+1` projector.

This gives the first parent-level version of the reduced sector split:

- one hidden phase-charge sector on `\Pi(u,v)` is designated as the zero-mass sector
- the opposite phase-charge sector is its complementary partner

The minimal parent-side zero-mass operator target is then:

$$
H_{\Pi}^{(0)} = P_{\Pi,-}\, H_{\Pi}^{(0)}\, P_{\Pi,-},
$$

with `P_{\Pi,-}` fixed as the parent preimage of `T1` under the chosen time orientation.

The more refined reading is now:

- phase covariance on `\Pi(u,v)` already forces `H_{\Pi}^{(0)}` to be diagonal in the `P_{\Pi,\pm}` basis
- the remaining burden is whether the selected direction `u` fixes one of those two sectors as the unique direct zero-mass traversal sector
- if it does, the one-sector support condition above follows immediately

The reduction problem is then no longer completely opaque. It becomes:

1. define a reduction map `\mathcal{R}` from the parent hidden-plane data to the reduced spinor branch
2. require
   $$
   \mathcal{R}(P_{\Pi,-}) = P,
   \qquad
   \mathcal{R}(P_{\Pi,+}) = Q
   $$
   in the reduced description
3. check whether
   $$
   \mathcal{R}(H_{\Pi}^{(0)}) = H_0
   $$
   then forces
   $$
   H_0 = P H_0 P, \qquad QH_0 = H_0Q = 0
   $$

This is still not a derivation, but it is the first concrete parent-side mechanism that could in principle generate the reduced projector identities instead of merely agreeing with them afterwards.

#### What this would actually show if it worked

If such a reduction map could be made explicit, the project would gain a real Route A bridge:

- the hidden complex line would carry the primitive phase-charge split
- the reduced `T1/T2` sectors would be images of that split
- the zero-mass operator would act on one hidden charge sector before reduction
- the reduced support of `H_0` on `T1` would therefore be inherited, not postulated

That is the strongest currently visible candidate for how Route A might actually be earned.

#### Toy-level reduction map `\mathcal{R}`

The next useful step is not a full construction, but a toy-level specification of what sort of map `\mathcal{R}` must be for the projector story even to make sense.

At minimum, `\mathcal{R}` should act on two kinds of parent objects:

1. states or sectors on the hidden complex line
2. operators acting on those sectors

So the most economical working picture is:

$$
\mathcal{R}_{\mathrm{vec}} :
\Pi(u,v)_{\mathbf{C}} \otimes S_{\mathrm{vis}}
\longrightarrow
\mathcal{H}_{\mathrm{spin}},
$$

with `S_{\mathrm{vis}}` a minimal visible carrier supplying the reduced `SU(2)` doublet structure, and

$$
\mathcal{R}_{\mathrm{op}}(A) :=
\mathcal{R}_{\mathrm{vec}}\, A\, \mathcal{R}_{\mathrm{vec}}^{-1}
$$

whenever that inverse or an effective partial inverse makes sense on the reduced image.

This is only a toy model, but it is enough to state the compatibility conditions.

#### Minimal choice of `S_{\mathrm{vis}}`

The smallest plausible choice is

$$
S_{\mathrm{vis}} \cong \mathbf{C}^2,
$$

interpreted as the visible `SU(2)` doublet carrier already present in the `Spin(2,3)` spinor decomposition.

Then the dimensional bookkeeping works in the simplest possible way:

- the real plane `\Pi(u,v)` becomes one complex line after choosing `J_\Pi`
- after complexification, that line splits into two one-dimensional phase-charge sectors
- each such sector tensored with `S_{\mathrm{vis}} \cong \mathbf{C}^2` gives a complex two-dimensional block

So the toy reduced space becomes

$$
\Pi(u,v)_{\mathbf{C}} \otimes S_{\mathrm{vis}}
\cong
(\mathbf{1}_{-} \otimes \mathbf{2}) \oplus (\mathbf{1}_{+} \otimes \mathbf{2}),
$$

which is exactly a `2 + 2` decomposition of a complex `4`-dimensional space.

This matches the reduced static structure

$$
\mathbf{4} = (\mathbf{2},-1/2) \oplus (\mathbf{2},+1/2),
$$

at the level of dimensions and charge splitting.

That does **not** prove the reduction map. But it shows that the toy parent bookkeeping is at least consistent with the known `Spin(2,3)` spinor structure.

#### Toy identification pattern

Under this minimal choice, the natural identification compatible with the static convention is:

$$
\mathbf{1}_{-} \otimes \mathbf{2} \longmapsto T1,
\qquad
\mathbf{1}_{+} \otimes \mathbf{2} \longmapsto T2,
$$

So the toy picture is:

- hidden phase charge supplies the `\pm` sector split
- the visible `SU(2)` carrier supplies the doublet multiplicity inside each sector
- together they reproduce the reduced four-component spinor as two doublets of opposite charge

This is the first place where the reduction picture and the static `Spin(2,3)` representation data genuinely lock together rather than merely coexist.

#### Minimal symmetry-compatibility requirement

Dimensional agreement by itself is too weak. The toy reduction should also respect the symmetry that is already visible on the reduced side.

On the parent toy space

$$
\Pi(u,v)_{\mathbf{C}} \otimes S_{\mathrm{vis}},
$$

there is a natural product action:

- `U(1)_\Pi` acts on the hidden phase-charge line
- `SU(2)_{\mathrm{vis}}` acts on `S_{\mathrm{vis}} \cong \mathbf{C}^2`

So the parent toy symmetry is

$$
U(1)_\Pi \times SU(2)_{\mathrm{vis}}.
$$

On the reduced `Spin(2,3)` spinor, the maximal compact subgroup is

$$
K = U(1) \times SU(2),
$$

with the decomposition

$$
\mathbf{4} = (\mathbf{2},-1/2) \oplus (\mathbf{2},+1/2).
$$

The reduction map should therefore satisfy a minimal intertwining condition:

$$
\mathcal{R}_{\mathrm{vec}}\big((e^{i\alpha},g)\cdot \psi\big)
=
\rho_K(e^{i\alpha},g)\,\mathcal{R}_{\mathrm{vec}}(\psi),
$$

at least at the toy level, where `\rho_K` is the reduced action of the maximal compact subgroup on the spinor.

In plain language:

- hidden phase charge should reduce to the `U(1)` charge measured by `J^{01}`
- the visible carrier `S_{\mathrm{vis}}` should reduce to the `SU(2)` doublet structure already present in each sector

If this intertwining fails, then the toy reduction would only be dimensional bookkeeping, not a representation-theoretic bridge.

If it holds, then the toy picture does more than count dimensions:

- it explains why each reduced sector is an `SU(2)` doublet
- it explains why the two sectors carry opposite `U(1)` charge
- it makes the toy reduction consistent with the known maximal compact structure of `Spin(2,3)`

#### Explicit toy action

The most economical toy action is to assign the hidden phase-charge weights directly as

$$
(e^{i\alpha},g)\cdot(\xi_- \otimes s)
=
e^{-i\alpha/2}\,\xi_- \otimes (g s),
$$
$$
(e^{i\alpha},g)\cdot(\xi_+ \otimes s)
=
e^{+i\alpha/2}\,\xi_+ \otimes (g s),
$$

with

- `\xi_- \in \mathbf{1}_-`
- `\xi_+ \in \mathbf{1}_+`
- `s \in \mathbf{2} \cong S_{\mathrm{vis}}`

So the parent toy representation is exactly

$$
(\mathbf{1}_{-} \otimes \mathbf{2}) \oplus (\mathbf{1}_{+} \otimes \mathbf{2})
$$

with `U(1)_\Pi` weights `-1/2` and `+1/2`.

Under the fixed identification

$$
\mathbf{1}_{-} \otimes \mathbf{2} \longmapsto T1,
\qquad
\mathbf{1}_{+} \otimes \mathbf{2} \longmapsto T2,
$$

the induced infinitesimal generator on the toy space is

$$
J_{\Pi,\mathrm{toy}}
= \frac12 K_{\Pi} \otimes \mathbf{1}_{\mathrm{vis}}
=
\begin{pmatrix}
-\tfrac12\,\mathbf{1}_2 & 0 \\
0 & +\tfrac12\,\mathbf{1}_2
\end{pmatrix},
$$

which matches the reduced block form already used for `J^{01}` in the static kernel. So once time orientation is fixed there is no extra local sign ambiguity left in the toy reduction: the hidden `(-)` phase-charge sector is exactly the parent preimage of `T1`.

So at the toy representation level:

- the hidden phase action reproduces the reduced `U(1)` charges
- the visible carrier reproduces the reduced `SU(2)` doublet structure
- the product action reproduces the maximal compact `U(1) \times SU(2)` decomposition of the spinor

This is not yet a proof that the full `Spin(2,3)` action is recovered. But it is the first explicit representation-level match, not just a dimensional one.

#### Explicit basis-level intertwiner `\mathcal{R}_{\mathrm{vec}}`

The toy reduction can now be written explicitly on basis vectors.

Choose a hidden charge basis

$$
K_{\Pi}\xi_- = -\xi_-,
\qquad
K_{\Pi}\xi_+ = +\xi_+,
$$

and a visible basis `s_1,s_2` of `S_{\mathrm{vis}} \cong \mathbf{C}^2`.

Then define the ordered parent basis

$$
f_1 := \xi_- \otimes s_1,
\qquad
f_2 := \xi_- \otimes s_2,
\qquad
f_3 := \xi_+ \otimes s_1,
\qquad
f_4 := \xi_+ \otimes s_2.
$$

On the reduced side, let `e_1,e_2,e_3,e_4` be the standard spinor basis adapted to the fixed `J^{01}` block decomposition, so that

**Notation warning.** Here `e_a` denotes a reduced *spinor-basis vector*. This symbol is unrelated to the octonionic imaginary basis units often also written as `e_1,\dots,e_7`. In this scaffold we reserve `u` for the selected octonionic imaginary direction (which may be gauge-fixed to a standard imaginary unit in a separate octonion basis if desired).

$$
T1 = \mathrm{span}_{\mathbf{C}}\{e_1,e_2\},
\qquad
T2 = \mathrm{span}_{\mathbf{C}}\{e_3,e_4\}.
$$

Define the vector-level reduction map by

$$
\mathcal{R}_{\mathrm{vec}}(f_a) = e_a,
\qquad a=1,2,3,4.
$$

In this basis, the parent toy charge generator is exactly

$$
J_{\Pi,\mathrm{toy}}
= \frac12 K_{\Pi}\otimes \mathbf{1}_{\mathrm{vis}}
=
\begin{pmatrix}
-\tfrac12\,\mathbf{1}_2 & 0 \\
0 & +\tfrac12\,\mathbf{1}_2
\end{pmatrix},
$$

so one has the exact intertwining relation

$$
\mathcal{R}_{\mathrm{vec}}\, J_{\Pi,\mathrm{toy}}
=
J^{01}\,\mathcal{R}_{\mathrm{vec}}.
$$

This is stronger than the earlier abstract compatibility statement: in the chosen basis, the parent and reduced charge generators are literally the same matrix.

#### Minimal parent-adapted basis-fixing conditions

The basis above should not be thought of as completely arbitrary. The parent toy structures already constrain it strongly.

On the hidden side, the charge operator `K_{\Pi}` fixes the decomposition

$$
\Pi(u,v)_{\mathbf C} = \mathbf C\,\xi_- \oplus \mathbf C\,\xi_+,
\qquad
K_{\Pi}\xi_- = -\xi_-,
\qquad
K_{\Pi}\xi_+ = +\xi_+.
$$

This still leaves a phase freedom on each eigenspace. The parent charge-flip involution removes the relative ambiguity: require

$$
C_\Pi \xi_- = \xi_+,
\qquad
C_\Pi \xi_+ = \xi_-.
$$

That fixes the hidden basis up to a common overall phase, which is harmless at the toy level.

On the visible side, the quaternionic `SU(2)` structure supplies an equally natural adapted basis. Regard `H(u,v)` as a complex two-dimensional space over `\mathbf C_u` and choose `s_1,s_2` so that

$$
L_u s_1 = s_1\,u,
\qquad
L_u s_2 = -\,s_2\,u,
$$

so `s_1,s_2` are opposite-weight eigenvectors for the visible Cartan generator `L_u`. Then fix the remaining exchange/phase ambiguity by requiring

$$
L_v s_1 = s_2,
\qquad
L_v s_2 = -\,s_1.
$$

Once these conditions are imposed, the ordered parent basis

$$
f_1 = \xi_- \otimes s_1,\quad
f_2 = \xi_- \otimes s_2,\quad
f_3 = \xi_+ \otimes s_1,\quad
f_4 = \xi_+ \otimes s_2
$$

is no longer chosen merely by hindsight from the reduced gamma basis. It is the minimal basis adapted simultaneously to

- hidden phase charge `K_{\Pi}`
- hidden charge flip `C_\Pi`
- visible Cartan generator `L_u`
- one visible ladder direction `L_v`

The residual freedom is now much smaller:

- a common global phase
- the global reversal that swaps the orientation of `u` together with time orientation

So the live question is narrower than before. The notes no longer need to ask "how do we choose any basis at all?" The sharper question is whether these parent-adapted basis-fixing conditions are themselves forced canonically by the octonionic reduction, or whether they remain the last local gauge choice.

#### Residual stabilizer after basis adaptation

It is useful to say exactly what survives after the basis-fixing conditions above.

Before adaptation, the toy carrier

$$
\Pi(u,v)_{\mathbf C} \otimes S_{\mathrm{vis}}
$$

admits independent basis changes on the hidden and visible factors. After imposing:

- hidden charge diagonalization by `K_\Pi`
- relative hidden phase fixing by `C_\Pi`
- visible Cartan diagonalization by `L_u`
- visible ladder normalization by `L_v`

the remaining stabilizer is very small.

At the toy level it reduces to:

1. a common overall complex phase
   $$
   f_a \mapsto e^{i\theta} f_a
   $$
   which does not change any generator matrices
2. the global orientation reversal
   $$
   u \mapsto -u,
   \qquad
   J_\Pi \mapsto -J_\Pi,
   \qquad
   K_\Pi \mapsto -K_\Pi,
   \qquad
   T1 \leftrightarrow T2
   $$
   provided the reduced time orientation is reversed with it

So the residual ambiguity is not a large hidden basis group anymore. It is essentially:

- one harmless `U(1)` phase
- one global `\mathbf Z_2` orientation choice

That is a real structural gain. The canonicity problem has become:

> can the ambient parent reduction, possibly through a scale-flow/readout vector above the reduced `Spin(2,3)` slice, fix the remaining global `\mathbf Z_2` orientation choice and the adapted basis up to harmless overall phase?

This is a much sharper question than the earlier vague request for a "canonical basis."

#### Readout orientation principle

The remaining `\mathbf Z_2` ambiguity can now be stated in a cleaner form.

At the toy level, the parent reduction data determine everything except the simultaneous reversal

$$
u \mapsto -u,
\qquad
K_\Pi \mapsto -K_\Pi,
\qquad
T1 \leftrightarrow T2,
\qquad
t \mapsto -t.
$$

So the residual ambiguity is not a large internal gauge freedom. It is the choice of which global orientation is to be called the physical forward/readout orientation.

If the selector belongs to a larger ambient scale geometry, this should be read as a descent problem rather than as an intrinsic `Spin(2,3)` choice. `Spin(2,3)` supplies the two-sector reduced representation. The ambient scale/readout flow supplies, if it exists, the orientation that tells the reduced theory which sector is the forward observable one.

This suggests the following disciplined principle:

> Physical orientation is fixed by requiring that the direct zero-mass readout channel and the forward coarse-grained evolution arrow agree.

In the present framework that means:

1. choose the time orientation for which the reduced semigroup acts forward on the observed sector
2. choose the hidden orientation so that its `(-)` charge sector maps to that same forward readout sector
3. call the resulting reduced sector `T1`

Under this principle, the residual `\mathbf Z_2` is not an extra unresolved hidden symmetry of the observable theory. It is the relative orientation between:

- the parent hidden line
- the reduced time orientation
- the observable readout arrow

What this does and does not achieve:

- it does explain why the last sign choice belongs with epistemics and dynamics rather than pure statics
- it does reduce the canonicity gap to a relative orientation or scale-flow descent principle
- it does **not** yet derive that principle from the octonionic parent or from a larger ambient scale geometry

So the honest current closure is:

- kinematics fixes the reduction almost completely
- the last `\mathbf Z_2` is fixed once the framework chooses, or derives from an ambient scale-flow selector, which orientation counts as forward observable readout
- whether that final step can be derived rather than chosen remains open

#### Minimal forward-semigroup criterion

The readout orientation principle can be stated more concretely in dynamical language.

The reduced observable theory is not just a static sector label. In the weak-coupling regime it is supposed to carry a forward coarse-grained evolution law of semigroup type:

$$
\rho_1(t) = e^{\,t\mathcal L_1}\rho_1(0),
\qquad
t \ge 0,
$$

on the observed sector, with `\mathcal L_1` the reduced generator and `H_0` its direct zero-mass part.

Under the residual global reversal,

$$
u \mapsto -u,
\qquad
T1 \leftrightarrow T2,
\qquad
t \mapsto -t,
$$

the two oriented candidate readout sectors are exchanged together with the direction of the reduced time arrow.

So the remaining `\mathbf Z_2` can be fixed by the following minimal criterion:

> choose the global orientation for which the direct zero-mass channel, the projected observable sector, and the forward reduced semigroup are all aligned.

Equivalently, the sector called `T1` is not merely the `J^{01}` block of eigenvalue `-1/2`; it is the block on which the framework places:

- direct zero-mass support
- observable readout
- forward reduced evolution for `t \ge 0`

This is stronger than a naming convention but weaker than a derivation from pure parent geometry. It says the last global orientation choice is fixed by demanding consistency between:

- parent hidden orientation
- reduced charge sector
- observational arrow
- coarse-grained dynamical arrow

So the live open question is now very specific:

- can the bulk parent dynamics or a larger ambient scale-flow geometry force this alignment, or must it remain a final framework principle?

One natural candidate for such a bulk forcing already exists elsewhere in the framework: the signed transport coupling `\kappa_u`. Because `\kappa_u` is odd under `u \mapsto -u`, any derivation that ties forward direct readout to the constructive/persistent side of the transport dynamics would automatically turn `\kappa_u` into an orientation selector rather than just a classification parameter.

The reduced transport equations sharpen this further. In the phase convention where the direct locked readout branch is normalized to `\Phi_*=0`, the persistence condition becomes

$$
\kappa_u \cosh(2\rho_*) > \gamma,
$$

so direct long-lived readout requires `\kappa_u > 0`. Under the residual global reversal `u \mapsto -u`, `\kappa_u` changes sign and constructive versus inverted orientation are exchanged. So the current best bulk-level orientation selector is:

- the physical readout orientation is the one for which the direct readout branch is constructive/persistent in the phase-normalized gauge

This is still not derived from the octonionic parent alone, but it is much sharper than leaving the last sign as a purely representational leftover.

That also means the `N2` blocker is no longer spread across several equally vague burdens. Three pieces are already conditionally in place:

1. hidden-line phase covariance makes the parent zero-mass operator charge diagonal
2. the reduction map is built to intertwine the parent charge generator with `J^{01}`
3. the residual sign dictionary is fixed up to the single global orientation reversal isolated above

So the live open step is now best stated as one final operational axiom:

> the unique direct readout branch is the phase-normalized locked branch lying on the constructive/persistent side of the transport dynamics, equivalently the branch with `\kappa_u > 0`.

Equivalently, in the ambient-selector reading:

> the sector called `T1` is the reduced name for the sector selected by the ambient forward scale/readout flow.

If that axiom is accepted, then the remaining `\mathbf Z_2` is fixed by the sign of `\kappa_u`, the chosen direct-support sector is identified with the parent `(-)` charge sector, and the reduced zero-mass operator satisfies

$$
H_0 = P H_0 P,
\qquad
QH_0 = 0,
\qquad
H_0Q = 0.
$$

So the honest current closure is:

- `N2` is conditionally closed once the constructive-readout axiom is adopted
- the real remaining derivation burden is to obtain that axiom from the octonionic bulk rather than merely accept it as the final operational rule
- this is a much more disciplined stopping point than the older situation, where the whole `T1` selection looked primitive

The same can be done for the compact `SU(2)` sector. Define parent visible generators

$$
\widetilde S_{23} := \mathbf{1}_{\mathrm{hid}} \otimes \Big(-\frac12\sigma^3\Big),
\qquad
\widetilde S_{34} := \mathbf{1}_{\mathrm{hid}} \otimes \Big(-\frac12\sigma^1\Big),
\qquad
\widetilde S_{42} := \mathbf{1}_{\mathrm{hid}} \otimes \Big(-\frac12\sigma^2\Big).
$$

In the gamma-matrix basis already chosen in the static kernel, these satisfy

$$
\mathcal{R}_{\mathrm{vec}}\, \widetilde S_{23}
=
J^{23}\,\mathcal{R}_{\mathrm{vec}},
$$
$$
\mathcal{R}_{\mathrm{vec}}\, \widetilde S_{34}
=
J^{34}\,\mathcal{R}_{\mathrm{vec}},
$$
$$
\mathcal{R}_{\mathrm{vec}}\, \widetilde S_{42}
=
J^{42}\,\mathcal{R}_{\mathrm{vec}}.
$$

So the present status is sharper than before:

- an explicit `\mathcal{R}_{\mathrm{vec}}` exists at the toy level
- it exactly intertwines the whole maximal compact `U(1)\times SU(2)` action in the chosen basis
- the sign dictionary and the `T1/T2` sector image are therefore no longer abstract desiderata at this level

What remains open is not compact-level existence but canonical parent interpretation: why this toy basis map and this toy generator set should be the ones singled out by the octonionic parent reduction.

#### Explicit off-diagonal image in the same basis

The same basis map also makes the toy noncompact sector explicit.

In the hidden charge basis `\xi_-,\xi_+`, define the charge-flip operators

$$
C_{\mathrm{hid}} :=
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix},
\qquad
D_{\mathrm{hid}} :=
\begin{pmatrix}
0 & -i \\
i & 0
\end{pmatrix}.
$$

On the visible carrier, define

$$
\tau_2 := \sigma^1,
\qquad
\tau_3 := \sigma^2,
\qquad
\tau_4 := \sigma^3.
$$

Then the parent toy off-diagonal generators are

$$
\widetilde X_{\hat a} := C_{\mathrm{hid}} \otimes \tau_{\hat a},
\qquad
\widetilde Y_{\hat a} := D_{\mathrm{hid}} \otimes \tau_{\hat a},
\qquad
\hat a \in \{2,3,4\}.
$$

Under the same ordered basis `f_1,\dots,f_4`, these are exactly the block matrices

$$
\widetilde X_{\hat a}
=
\begin{pmatrix}
0 & \tau_{\hat a} \\
\tau_{\hat a} & 0
\end{pmatrix},
\qquad
\widetilde Y_{\hat a}
=
\begin{pmatrix}
0 & -i\tau_{\hat a} \\
i\tau_{\hat a} & 0
\end{pmatrix}.
$$

So the vector-level intertwiner carries them directly into the reduced off-diagonal families:

$$
\mathcal{R}_{\mathrm{vec}}\, \widetilde X_{\hat a}\, \mathcal{R}_{\mathrm{vec}}^{-1}
=
\begin{pmatrix}
0 & \tau_{\hat a} \\
\tau_{\hat a} & 0
\end{pmatrix},
$$
$$
\mathcal{R}_{\mathrm{vec}}\, \widetilde Y_{\hat a}\, \mathcal{R}_{\mathrm{vec}}^{-1}
=
\begin{pmatrix}
0 & -i\tau_{\hat a} \\
i\tau_{\hat a} & 0
\end{pmatrix}.
$$

In the chosen gamma-matrix basis, the reduced mixed generators satisfy the exact identities

$$
J^{0\hat a}
=
-\frac{i}{2}\,
\mathcal{R}_{\mathrm{vec}}\, \widetilde X_{\hat a}\, \mathcal{R}_{\mathrm{vec}}^{-1},
\qquad
J^{1\hat a}
=
\frac{i}{2}\,
\mathcal{R}_{\mathrm{vec}}\, \widetilde Y_{\hat a}\, \mathcal{R}_{\mathrm{vec}}^{-1},
\qquad
\hat a \in \{2,3,4\}.
$$

So at the toy matrix level the explicit intertwiner already reaches the whole `10`-generator set:

- compact sector: exact
- off-diagonal sector: exact
- Cartan-style `4+6` split: exact

This materially changes the status of the reduction programme. The live open problem is no longer whether one can write down a basis-level map whose image has the right matrices. One can. The live problem is whether these toy parent operators arise canonically from the octonionic parent geometry rather than being selected after the fact in the reduced basis.

#### Beyond the maximal compact subgroup

The next sharp test is whether this bridge extends beyond

$$
K = U(1) \times SU(2)
$$

to more of the full `Spin(2,3)` action.

At the toy matrix level, the answer is now yes. What remains open is whether that extension is genuinely parent-side and canonical rather than only an exact reconstruction in the chosen reduced basis.

At the Lie-algebra level one has the Cartan decomposition

$$
\mathfrak{so}(2,3) = \mathfrak{k} \oplus \mathfrak{p},
\qquad
\mathfrak{k} \cong \mathfrak{u}(1) \oplus \mathfrak{su}(2),
$$

with

$$
[\mathfrak{k},\mathfrak{k}] \subset \mathfrak{k},
\qquad
[\mathfrak{k},\mathfrak{p}] \subset \mathfrak{p},
\qquad
[\mathfrak{p},\mathfrak{p}] \subset \mathfrak{k}.
$$

The toy bridge already addresses the `\mathfrak{k}` part:

- hidden phase charge -> the `\mathfrak{u}(1)` generator seen as `J^{01}`
- visible doublet carrier -> the `\mathfrak{su}(2)` action on each sector

What is missing is the parent-side origin of the `\mathfrak{p}` part, i.e. the generators that do not preserve the two charge sectors separately.

At the reduced spinor level, these are exactly the operators that mix `T1` and `T2`. So the next extension problem is:

> can one identify a parent family of operators on `\Pi(u,v)_{\mathbf{C}} \otimes S_{\mathrm{vis}}` whose reduced image lands in the off-diagonal `T1/T2` blocks and closes with the compact generators into the `\mathfrak{so}(2,3)` commutator structure?

The safest current candidate is that the noncompact sector should come from operators that:

- change the hidden phase charge
- act nontrivially on the visible `SU(2)` carrier
- therefore link `\mathbf{1}_{-} \otimes \mathbf{2}` to `\mathbf{1}_{+} \otimes \mathbf{2}`

So the first toy extension target is not yet the whole group. It is the existence of a parent operator space `\mathcal{P}_{\mathrm{toy}}` such that:

$$
\mathcal{P}_{\mathrm{toy}} :
\mathbf{1}_{-} \otimes \mathbf{2}
\longleftrightarrow
\mathbf{1}_{+} \otimes \mathbf{2},
$$

and such that, together with the compact generators, its reduced image obeys the expected closure relations.

If that fails, then the current bridge only explains the maximal compact subgroup.

If it works, then the bridge has a credible route from hidden phase data to the full reduced `Spin(2,3)` structure.

#### What would count as progress here

The next nontrivial gain would be any one of the following:

1. a toy basis for `\mathcal{P}_{\mathrm{toy}}` whose reduced image is visibly off-diagonal in the `T1/T2` decomposition
2. a commutator calculation showing that the compact toy generators and `\mathcal{P}_{\mathrm{toy}}` close in the same pattern as `\mathfrak{k} \oplus \mathfrak{p}`
3. a clear obstruction showing that the current parent toy space is too small, forcing enlargement of the parent carrier before a full bridge can exist

#### First toy candidate for `\mathcal{P}_{\mathrm{toy}}`

There is a natural first guess for the noncompact toy sector.

Keep the compact generators in block form:

$$
J_{\mathrm{toy}} =
\begin{pmatrix}
-\tfrac12\,\mathbf{1}_2 & 0 \\
0 & +\tfrac12\,\mathbf{1}_2
\end{pmatrix},
\qquad
S_a =
\begin{pmatrix}
\tfrac12\sigma_a & 0 \\
0 & \tfrac12\sigma_a
\end{pmatrix},
\qquad a=1,2,3.
$$

Then define the off-diagonal triplet generators

$$
X_a =
\begin{pmatrix}
0 & \sigma_a \\
\sigma_a & 0
\end{pmatrix},
\qquad
Y_a =
\begin{pmatrix}
0 & -i\sigma_a \\
i\sigma_a & 0
\end{pmatrix},
\qquad a=1,2,3.
$$

The real span

$$
\mathcal{P}_{\mathrm{toy}} =
\mathrm{span}_{\mathbf{R}}\{X_1,X_2,X_3,Y_1,Y_2,Y_3\}
$$

has dimension `6`, which is exactly the right dimension for the noncompact complement `\mathfrak{p}` in

$$
\mathfrak{so}(2,3) = \mathfrak{k} \oplus \mathfrak{p}.
$$

This is already encouraging: it is the first toy operator space with the correct size, the correct off-diagonal `T1/T2` support, and the correct visible `SU(2)` triplet labeling.

#### Why this candidate is natural

It is not arbitrary.

- off-diagonal support means these operators mix `T1` and `T2`, as noncompact generators should
- the Pauli triplet gives the visible `SU(2)` adjoint structure
- the pair `(X_a,Y_a)` for each `a` behaves like a two-component object under the hidden phase rotation generated by `J_{\mathrm{toy}}`

Equivalently, if one defines

$$
Z_a^{\pm} := X_a \pm iY_a,
$$

then the `Z_a^\pm` are the natural charge-raising and charge-lowering combinations: they move states between the two phase-charge sectors.

At the toy level, this is exactly the behavior one would want from the noncompact part of the bridge.

#### More parent-side reading of the noncompact sector

The off-diagonal Pauli-triplet picture can now be rewritten in a more genuinely parent-side way.

On the real hidden plane `\Pi(u,v) = \mathrm{span}_{\mathbf{R}}\{v,uv\}`, fix a real-linear involution `C_\Pi` by

$$
C_\Pi(v) = v,
\qquad
C_\Pi(uv) = -\,uv.
$$

Then `C_\Pi` anticommutes with the hidden complex structure:

$$
C_\Pi J_\Pi = - J_\Pi C_\Pi.
$$

So after complexification, `C_\Pi` exchanges the two hidden phase-charge sectors. Define also

$$
D_\Pi := J_\Pi C_\Pi,
$$

which gives the second independent charge-flipping direction. Together, `C_\Pi` and `D_\Pi` are the natural parent-side analogues of the two off-diagonal charge-changing directions.

On the same local quaternionic slice, let

$$
L_u,\; L_v,\; L_{uv}
$$

be left multiplication by the three imaginary quaternion units. These generate the visible `\mathfrak{su}(2)` action on the complex two-dimensional carrier.

This gives a more intrinsic parent candidate for the noncompact sector:

$$
\mathcal{P}_{\mathrm{parent,toy}}
=
\mathrm{span}_{\mathbf{R}}
\{
C_\Pi \otimes L_u,\;
C_\Pi \otimes L_v,\;
C_\Pi \otimes L_{uv},\;
D_\Pi \otimes L_u,\;
D_\Pi \otimes L_v,\;
D_\Pi \otimes L_{uv}
\}.
$$

Its dimension is again `2 \times 3 = 6`, but now each factor has a direct parent meaning:

- `C_\Pi, D_\Pi` are hidden charge-flipping operators
- `L_u, L_v, L_{uv}` are the visible quaternionic `SU(2)` generators

So the toy noncompact sector can be read as:

> charge flip on the hidden plane tensor visible quaternionic rotation.

That is conceptually much better than treating the six off-diagonal generators as unexplained matrix blocks.

#### Why this helps

This parent-side factorization explains the earlier toy `X_a,Y_a` pattern:

- the hidden `2` comes from operators that anticommute with the complex structure and therefore exchange the `\pm` charge sectors
- the visible `3` comes from the quaternionic imaginary triplet acting by left multiplication

So the `2 \times 3 = 6` count is no longer just a coincidence. It is the natural product of:

- one hidden charge-flip doublet
- one visible `SU(2)` adjoint triplet

#### Hidden three-generator algebra on the plane

The hidden operators on `\Pi(u,v)` are not arbitrary either. They already form a closed three-generator system.

Recall:

$$
J_\Pi^2 = -1,
\qquad
C_\Pi^2 = +1,
\qquad
D_\Pi = J_\Pi C_\Pi.
$$

From `C_\Pi J_\Pi = -J_\Pi C_\Pi`, one gets

$$
[J_\Pi,C_\Pi] = 2D_\Pi,
$$
$$
[J_\Pi,D_\Pi] = -2C_\Pi,
$$
$$
[C_\Pi,D_\Pi] = -2J_\Pi.
$$

So the hidden plane already carries a closed `3`-generator algebra made from:

- one phase generator `J_\Pi`
- two charge-flipping generators `C_\Pi, D_\Pi`

This is the hidden-side origin of the earlier `U(1)` plus charge-flip doublet picture.

The noncompact parent toy sector then appears naturally as:

$$
\{C_\Pi,D_\Pi\}
\otimes
\{L_u,L_v,L_{uv}\},
$$

while the compact part uses:

$$
J_\Pi
\otimes
1,
\qquad
1
\otimes
\{L_u,L_v,L_{uv}\}.
$$

So even before reduction, the parent toy structure already splits into:

- one hidden phase generator
- one hidden charge-flip pair
- one visible quaternionic `SU(2)` triplet

That is exactly the structural content needed for the later

$$
\mathfrak{k} \oplus \mathfrak{p}
=
(\mathfrak{u}(1)\oplus\mathfrak{su}(2))
\oplus
(\mathbf{2}\otimes\mathbf{3})
$$

bookkeeping.

#### What still needs to be checked

The candidate becomes genuinely useful only if its commutators behave correctly.

The next checks are:

1. `[\mathfrak{k}_{\mathrm{toy}}, \mathcal{P}_{\mathrm{toy}}] \subset \mathcal{P}_{\mathrm{toy}}`
2. `[\mathcal{P}_{\mathrm{toy}}, \mathcal{P}_{\mathrm{toy}}] \subset \mathfrak{k}_{\mathrm{toy}}`
3. the `U(1)` action generated by `J_{\mathrm{toy}}` rotates `(X_a,Y_a)` into one another with the expected charge pattern
4. the `SU(2)` action generated by the `S_a` rotates the index `a` as a triplet

If those checks work, the toy bridge will have passed its first full Lie-algebra consistency test.

#### Toy commutator check

With the conventions above, the commutators close in the expected pattern up to normalization conventions.

For the compact action:

$$
[S_a,S_b] = i\epsilon_{abc} S_c,
$$

so the `S_a` form the visible `\mathfrak{su}(2)` algebra.

The compact generators act on the off-diagonal sector as

$$
[S_a,X_b] = i\epsilon_{abc} X_c,
\qquad
[S_a,Y_b] = i\epsilon_{abc} Y_c,
$$

so both `X_b` and `Y_b` transform as `SU(2)` triplets.

For the hidden phase generator:

$$
[J_{\mathrm{toy}},X_a] = -i Y_a,
\qquad
[J_{\mathrm{toy}},Y_a] = +i X_a,
$$

so the pair `(X_a,Y_a)` is rotated by the `U(1)` charge generator exactly as expected. Equivalently,

$$
[J_{\mathrm{toy}}, Z_a^\pm] = \pm Z_a^\pm
$$

up to the overall normalization convention for `J_{\mathrm{toy}}`.

Finally, the noncompact sector closes back into the compact one:

$$
[X_a,X_b] = 4i\epsilon_{abc} S_c,
\qquad
[Y_a,Y_b] = 4i\epsilon_{abc} S_c,
\qquad
[X_a,Y_b] = -4i\,\delta_{ab}\, J_{\mathrm{toy}}.
$$

So, schematically,

$$
[\mathfrak{k}_{\mathrm{toy}},\mathcal{P}_{\mathrm{toy}}] \subset \mathcal{P}_{\mathrm{toy}},
\qquad
[\mathcal{P}_{\mathrm{toy}},\mathcal{P}_{\mathrm{toy}}] \subset \mathfrak{k}_{\mathrm{toy}},
$$

which is exactly the `\mathfrak{k} \oplus \mathfrak{p}` closure pattern one wants.

This does **not** prove that the toy algebra is canonically identical to the chosen `\mathfrak{so}(2,3)` basis. But it is the first place where the bridge has passed more than a bookkeeping test:

- dimension count: works
- maximal compact representation match: works
- candidate noncompact closure pattern: works

That is a substantial strengthening of the toy reduction picture.

#### Candidate basis-level dictionary

Using the explicit gamma-matrix realization already fixed in the static kernel,

$$
\gamma^0 = i\sigma^2 \otimes \mathbf{1}_2,\qquad
\gamma^1 = i\sigma^1 \otimes \mathbf{1}_2,
$$
$$
\gamma^2 = \sigma^3 \otimes \sigma^1,\qquad
\gamma^3 = \sigma^3 \otimes \sigma^2,\qquad
\gamma^4 = \sigma^3 \otimes \sigma^3,
$$

the Lie algebra generators

$$
J^{\mu\nu} = \frac{i}{4}[\gamma^\mu,\gamma^\nu]
$$

admit a basis-level reading that matches the toy bridge up to relabeling, sign, and normalization conventions.

Write `\tau_a := \sigma_a` for the visible Pauli triplet acting on the second tensor factor, with `a=1,2,3` corresponding to the spatial labels `(2,3,4)` up to relabeling.

Then:

1. the compact `U(1)` generator is
   $$
   J^{01}
   =
   -\frac12
   \begin{pmatrix}
   \mathbf{1}_2 & 0\\
   0 & -\mathbf{1}_2
   \end{pmatrix},
   $$
   which matches `J_{\mathrm{toy}}`

2. the spatial rotation generators `J^{23}, J^{34}, J^{42}` are block-diagonal and proportional to
   $$
   \mathbf{1}_2 \otimes \tau_a,
   $$
   so they match the toy compact triplet `S_a` up to basis choice in the spatial index

3. the mixed generators `J^{0\hat a}` and `J^{1\hat a}` with `\hat a \in \{2,3,4\}` are off-diagonal and proportional to
   $$
   \sigma^1 \otimes \tau_a,
   \qquad
   i\sigma^2 \otimes \tau_a,
   $$
   respectively, so they match the toy noncompact triplets `X_a` and `Y_a` up to normalization and sign conventions

This is the first explicit dictionary:

$$
J_{\mathrm{toy}} \leftrightarrow J^{01},
$$
$$
S_a \leftrightarrow \text{spatial rotation triplet } J^{23},J^{34},J^{42},
$$
$$
X_a,Y_a \leftrightarrow \text{mixed-generator triplets } J^{0\hat a},J^{1\hat a}.
$$

The important point is not the exact sign of each basis element. The important point is that:

- the compact toy generators line up with the compact reduced generators
- the off-diagonal toy generators line up with the reduced generators that mix `T1` and `T2`
- together they supply the right `10 = 4 + 6` basis count for `\mathfrak{so}(2,3)`

So the toy bridge has now reached the level of an explicit basis-level candidate, not just an abstract closure pattern.

#### What is still not settled

Even with this dictionary, some real gaps remain:

- the basis identification is not yet canonical
- the normalization and sign conventions have not been fixed by a single parent principle
- the map is still built from the reduced gamma-matrix realization rather than derived directly from the octonionic parent

So the honest status is:

- explicit toy basis-level match: available
- canonical parent derivation of that basis match: still open

#### Parent-side candidate for the visible Pauli triplet

There is now a much cleaner parent candidate for the visible `SU(2)` than simply importing the Pauli matrices from the reduced gamma basis.

Inside the local quaternionic slice

$$
H(u,v) = \mathrm{span}_{\mathbf{R}}\{1,u,v,uv\},
$$

there are two natural actions:

1. **right multiplication by `u`**
   - this gives the complex structure already used for the hidden phase direction
2. **left multiplication by the imaginary quaternion units**
   - this gives a natural `\mathfrak{su}(2)` action

The key structural point is that in the associative quaternionic slice, left and right multiplication commute:

$$
L_q R_u = R_u L_q
\qquad
(q \in H(u,v)).
$$

So the hidden phase `U(1)` and the visible `SU(2)` can arise from commuting parent-side structures rather than from unrelated postulates.

#### Minimal realization on a complex two-dimensional carrier

Regard `H(u,v)` as a complex vector space over `\mathbf{C}_u` using right multiplication by `u`. Then it has complex dimension `2`, with a convenient basis

$$
e_1 = 1, \qquad e_2 = v.
$$

In this basis:

- right multiplication by `u` gives the hidden complex structure
- left multiplication by `u`, `v`, and `uv` gives three complex-linear endomorphisms of the same two-dimensional space

Their action is:

$$
L_u(e_1) = e_1\,u,
\qquad
L_u(e_2) = -\,e_2\,u,
$$

so `L_u` acts as the diagonal Pauli generator;

$$
L_v(e_1) = e_2,
\qquad
L_v(e_2) = -e_1,
$$

so `L_v` acts as an off-diagonal Pauli generator;

and

$$
L_{uv}(e_1) = -\,e_2\,u,
\qquad
L_{uv}(e_2) = -\,e_1\,u,
$$

so `L_{uv}` gives the third Pauli-type generator.

Up to the usual basis and normalization conventions, this is exactly the Pauli triplet.

So the visible carrier `S_{\mathrm{vis}} \cong \mathbf{C}^2` no longer needs to be introduced as a free extra factor. A cleaner toy reading is:

$$
S_{\mathrm{vis}}
\cong
H(u,v)
\quad\text{as a complex vector space over } \mathbf{C}_u,
$$

with

- hidden phase structure from the right `\mathbf{C}_u` action
- visible `SU(2)` structure from left multiplication by the imaginary quaternion units

#### Why this is a real improvement

This is the first place where the bridge gives a parent-side source for both parts of the maximal compact subgroup at once:

- `U(1)` from right multiplication by the selected imaginary direction
- `SU(2)` from left multiplication inside the same quaternionic slice

and the two structures commute automatically inside the associative quaternionic carrier.

That is much stronger than merely tensoring an unexplained visible `\mathbf{2}` onto the hidden phase line.

#### Parent-toy commutator check

The decisive point is that this parent-side factorization already reproduces the right closure pattern at the toy level.

Let

$$
K_0 := J_\Pi \otimes 1,
\qquad
K_a := 1 \otimes L_a,
\qquad
P_{C,a} := C_\Pi \otimes L_a,
\qquad
P_{D,a} := D_\Pi \otimes L_a,
$$

where `L_a` stands for the visible quaternionic triplet `L_u, L_v, L_{uv}` with the obvious relabeling.

Using

$$
[J_\Pi,C_\Pi] = 2D_\Pi,
\qquad
[J_\Pi,D_\Pi] = -2C_\Pi,
\qquad
[C_\Pi,D_\Pi] = -2J_\Pi,
$$

and the quaternionic left-multiplication relations

$$
[L_a,L_b] = 2\epsilon_{abc}L_c,
\qquad
\{L_a,L_b\} = -2\delta_{ab}\,1,
$$

one gets the following parent-side toy commutators.

For the compact sector:

$$
[K_a,K_b] = 2\epsilon_{abc}K_c,
\qquad
[K_0,K_a] = 0.
$$

So `K_0` and the `K_a` already realize the expected compact `\mathfrak{u}(1)\oplus\mathfrak{su}(2)` structure up to normalization.

For compact acting on noncompact:

$$
[K_0,P_{C,a}] = 2P_{D,a},
\qquad
[K_0,P_{D,a}] = -2P_{C,a},
$$

and

$$
[K_a,P_{C,b}] = 2\epsilon_{abc}P_{C,c},
\qquad
[K_a,P_{D,b}] = 2\epsilon_{abc}P_{D,c}.
$$

So the noncompact sector transforms as:

- a hidden charge-flip doublet under `K_0`
- a visible triplet under the quaternionic `SU(2)`

Finally, the noncompact sector closes back into the compact one:

$$
[P_{C,a},P_{C,b}] = 2\epsilon_{abc}K_c,
\qquad
[P_{D,a},P_{D,b}] = 2\epsilon_{abc}K_c,
$$

and

$$
[P_{C,a},P_{D,b}] = 2\delta_{ab}K_0.
$$

So, at the parent toy level,

$$
[\mathfrak{k}_{\mathrm{parent,toy}},\mathfrak{k}_{\mathrm{parent,toy}}]\subset \mathfrak{k}_{\mathrm{parent,toy}},
\qquad
[\mathfrak{k}_{\mathrm{parent,toy}},\mathfrak{p}_{\mathrm{parent,toy}}]\subset \mathfrak{p}_{\mathrm{parent,toy}},
\qquad
[\mathfrak{p}_{\mathrm{parent,toy}},\mathfrak{p}_{\mathrm{parent,toy}}]\subset \mathfrak{k}_{\mathrm{parent,toy}},
$$

with the right `4 + 6` dimensional split.

This is a stronger statement than the earlier block-matrix closure check. The same closure pattern now appears directly from:

- hidden phase-plus-charge-flip structure on the plane
- visible quaternionic left-multiplication structure

before one matches anything to the reduced gamma-matrix basis.

#### What this does and does not establish

What it establishes:

- the parent toy ingredients are sufficient to realize the right algebraic shape
- the `2 \times 3 = 6` noncompact sector is structurally natural, not ad hoc
- the compact/noncompact split can be read directly from parent-side operators

What it does not yet establish:

- that this parent toy algebra is canonically the physically relevant one
- that the normalization and signature conventions are fixed uniquely
- that the full octonionic parent reduction forces exactly this slice and this operator choice

So this is not the final derivation, but it is the first real obstruction test that the parent-side bridge has passed.

#### Non-blocking interpretation of the quaternionic sector

At this point the project does not need to decide that the quaternionic slice is a new physical sector.

The safer reading is:

- the quaternionic slice is part of the octonionic basis reduction
- it supplies a local geometric carrier for hidden complex directions and their mixing
- its `SU(2)` structure is reduction geometry or bookkeeping for the reduced doublet structure
- the unresolved canonical status of that slice is a real hole, but not a reason to stop the rest of the program

So the quaternionic-sector question can now be bracketed as follows:

> it is strong enough to organize the reduction story locally, but not yet strong enough to demand promotion into new fundamental physics

This means the remaining tasks here should be treated as:

- valuable bridge work
- important for cleanup and conceptual honesty
- but non-blocking for the rest of the framework unless later results force a stronger interpretation

#### Minimal compatibility conditions

For Route A, the reduction map should satisfy at least:

1. **Charge-projector compatibility**
   $$
   \mathcal{R}_{\mathrm{op}}(P_{\Pi,-}) = P,
   \qquad
   \mathcal{R}_{\mathrm{op}}(P_{\Pi,+}) = Q
   $$
   with `P = P_{\mathrm{obs}}` the `J^{01}` eigenspace projector selected by the forward readout orientation, conventionally named `T1`, and `Q = 1-P`

2. **Zero-mass support compatibility**
   $$
   \mathcal{R}_{\mathrm{op}}(H_{\Pi}^{(0)}) = H_0
   $$
   with
   $$
   H_{\Pi}^{(0)} = P_{\Pi,-} H_{\Pi}^{(0)} P_{\Pi,-}
   $$

3. **Sector-image compatibility**
   the image of the parent `(-)` charge sector lands in the sector named `T1` after orientation is fixed, and the image of the parent `(+)` charge sector lands in the opposite sector named `T2`

4. **No spurious support**
   reduction should not create `T2` support for a parent operator that was already confined to the parent `(-)` charge sector

If those conditions hold, then the reduced identities

$$
H_0 = P H_0 P,
\qquad
QH_0 = H_0Q = 0
$$

follow by functorial transport of support, rather than by a separate ansatz.

#### Support preservation from a charge-generator intertwiner

The compatibility conditions above can be repackaged more economically.

Let

$$
J_{\Pi,\mathrm{toy}} = \frac12 K_{\Pi} \otimes \mathbf{1}_{\mathrm{vis}}
$$

on the parent toy space and let `J^{01}` be the fixed reduced charge generator on `\mathcal{H}_{\mathrm{spin}}`. If the vector-level reduction map satisfies the intertwining condition

$$
\mathcal{R}_{\mathrm{vec}}\, J_{\Pi,\mathrm{toy}}
=
J^{01}\, \mathcal{R}_{\mathrm{vec}},
$$

then the whole spectral dictionary follows automatically.

Because `W_-` and `W_+` are the eigenspaces of `J_{\Pi,\mathrm{toy}}` with eigenvalues `-1/2` and `+1/2`, while the reduced sectors named `T1` and `T2` are the eigenspaces of `J^{01}` with the same eigenvalues after orientation is fixed, the intertwining condition forces

$$
\mathcal{R}_{\mathrm{vec}}(W_-) \subseteq T1,
\qquad
\mathcal{R}_{\mathrm{vec}}(W_+) \subseteq T2.
$$

If `\mathcal{R}_{\mathrm{vec}}` is onto the reduced branch, this becomes

$$
\mathcal{R}_{\mathrm{vec}}(W_-) = T1,
\qquad
\mathcal{R}_{\mathrm{vec}}(W_+) = T2.
$$

Then, at the operator level,

$$
\mathcal{R}_{\mathrm{op}}(P_{\Pi,-}) = P,
\qquad
\mathcal{R}_{\mathrm{op}}(P_{\Pi,+}) = Q,
$$

and any parent operator supported only on `W_-` reduces automatically to an operator supported only on `T1`.

So a stronger but cleaner Route A statement is available:

- if the reduction intertwines the parent and reduced charge generators
- and the parent zero-mass operator is supported on `W_-`

then the reduced zero-mass operator support identities follow without needing an extra no-spurious-support postulate.

This is useful because it pushes part of the old `N2` burden back into the `N1` reduction problem, where it belongs. The live question is no longer "can the reduction somehow preserve support?" but "can the reduction be built as a charge-generator intertwiner?"

#### What remains underspecified

Several things are still open even in this toy picture:

- what exactly `S_{\mathrm{vis}}` should be before the full `Spin(2,3)` branch is reconstructed
- whether `\mathcal{R}_{\mathrm{vec}}` is injective, surjective onto the reduced branch, or only defined up to gauge
- whether `\mathcal{R}_{\mathrm{op}}` should be an algebra homomorphism, a partial intertwiner, or only a support-preserving coarse-graining map

But these are now the right open questions. They are much sharper than the earlier vague hope that some unspecified reduction would "explain" the `T1` block.

This is the first concrete place where Route A can stop being a slogan and become a derivation target.

Until then, the project should say:

- Route A closure condition: known in operator form, not yet derived

---

## Immediate work sequence

The fastest honest sequence from here is:

1. write the algebraic form of `R1`
2. write the generator-level version of `R2`
3. write the reduced decomposition for `R3`
4. decide whether the readout selector is internal to the parent octonionic reduction or descends from a larger scale-flow geometry
5. only then revisit the epistemic burden in `R4`

This order matters because the project should not try to justify `T1` before it has said clearly what `T1` is the reduction of, or whether `T1` is merely the reduced name for a sector selected by an ambient flow.

---

## Interfaces to current files

### From `core/parent-inquiry-map.md`

- use `u^\perp \cong \mathbf{C}^3` as the parent anchor
- treat the local quaternionic slice as the best current carrier of hidden complex-plane data

### From `core/master-framework.md`

- keep the ambient-to-observable reduction as the named bridge object
- preserve the distinction between ambient, effective, and observable levels

### From `kernels/statics.md`

- treat the current folding picture as a working proposal, not a theorem
- use the `T1/T2` split and `J^{01}` grading as reduced outputs, not unexplained inputs

### To `kernels/dynamics.md`

- once `R1-R3` are sharper, the bulk origin of the two-branch variables can be attacked in a less ad hoc way

### To `kernels/epistemics.md`

- `R4` is where the observational rule should be tied back to reduction rather than floating independently

---

## What success would look like

This scaffold will have done its job if the project can eventually state:

1. what the parent variables are
2. what is reduced away
3. what becomes the hidden complex plane
4. what becomes the `Spin(2,3)` branch
5. what supplies the scale/readout orientation, if it is not internal to `Spin(2,3)`
6. what becomes `T1/T2`
7. what finally becomes observable

That is the missing-middle statement the project currently owes most.
