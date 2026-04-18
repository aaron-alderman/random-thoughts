# Molecular Physics and Chemical Bonding

This note covers the first level where atomic building blocks form structured compounds with new internal degrees of freedom. The focus here is on bonding, vibrational and rotational structure, symmetry classification, and spectroscopy.

## Core Topics

### Born-Oppenheimer Approximation

The first organizing move in molecular physics is the separation of slow nuclei from fast electrons. Born-Oppenheimer does not remove coupling absolutely, but it creates the basic atlas picture: electronic structure defines a potential surface, and nuclear motion explores that surface as vibration, rotation, and reaction geometry.

For H2 the logic is especially clear:

1. Hold the proton-proton separation `R` fixed.
2. Solve the electronic problem at that `R`.
3. Add nuclear repulsion to obtain an effective potential.
4. Quantize nuclear motion in that potential.

This is the first major place where the atlas becomes explicitly layered. Fast electronic structure does not disappear; it becomes the landscape on which slower nuclear motion takes place.

The approximation works numerically as well as conceptually. Protons are about 1836 times heavier than electrons, so electronic adjustment is far faster than nuclear motion. For simple molecules like `H_2`, that makes the Born-Oppenheimer approximation extraordinarily good in practice, with failures showing up mainly in precision spectroscopy or near electronic-state crossings.

That is why the molecular atlas can begin with a potential-energy-surface picture without pretending the full coupled problem is solved exactly. The approximation is not a philosophical simplification; it is a quantitatively justified hierarchy of time and mass scales.

### The Heitler-London Picture and Exchange Bonding

The Heitler-London treatment is the molecular analogue of helium exchange physics becoming chemically visible. The bond is not captured by a purely classical Coulomb story; it emerges because the symmetrized quantum state lowers energy through exchange and creates a stable bonding combination.

In schematic form the two-electron wavefunction is built from the two atomic centers:

```text
phi_A(1) phi_B(2) +/- phi_B(1) phi_A(2)
```

The plus combination produces bonding and the minus combination antibonding when paired with the correct spin symmetry. The manuscript's main claim here is direct: the classical Coulomb picture alone does not explain the bond. The exchange term is the decisive quantum ingredient.

This is why molecular bonding belongs naturally after helium. The same exchange logic that split atomic spin sectors now becomes the mechanism of chemical stability.

The manuscript also preserves the more explicit balance of terms. The exchange integral is the distinctly quantum contribution, while Coulomb terms alone do not explain the binding pattern. In that sense, the covalent bond is not "electrostatics with ornamentation"; it is a lower-energy reorganized wavefunction whose stability relies on delocalization and exchange.

That is one of the cleanest places where chemistry begins to emerge from quantum mechanics without being reducible to classical pictures of forces between little balls.

### Ortho and Para Hydrogen

Hydrogen's nuclear-spin statistics show that spin symmetry is not only an electronic story. Ortho and para hydrogen sort rotational states by nuclear symmetry, which turns a subtle permutation rule into a thermodynamic and engineering reality for low-temperature hydrogen handling.

The key rule is:

- orthohydrogen: symmetric nuclear-spin state -> odd rotational `J`
- parahydrogen: antisymmetric nuclear-spin state -> even rotational `J`

At room temperature the statistical weights favor the ortho form, while at very low temperature the system tends toward the para ground state. The long conversion time without catalysts is a reminder that a symmetry rule can have very practical thermodynamic consequences.

The practical consequence is strong enough that it belongs in the atlas as more than an anecdote. Ordinary hydrogen stored cold slowly converts from the room-temperature ortho-rich mixture toward the para ground state, releasing heat in the process. That is why para-hydrogen preparation matters in cryogenic engineering and rocket-fuel handling: a symmetry rule about nuclear spin turns into a real macroscopic constraint on storage stability.

### Normal Modes and the Harmonic Approximation

Near equilibrium, molecules decompose into independent normal modes, which is one of the cleanest examples of complex many-coordinate motion becoming tractable by symmetry and linearization. The harmonic approximation then provides the base spectrum from which real spectroscopy starts to deviate.

After removing rigid translation and rotation, an `N`-atom molecule has:

- `3N - 6` vibrational modes if nonlinear
- `3N - 5` vibrational modes if linear

Near equilibrium the Hessian diagonalizes into independent oscillators with energies of the form

```text
E_vib = sum_k hbar omega_k (v_k + 1/2)
```

This is one of the manuscript's most useful recurring examples of "complicated coordinates become simple after the right symmetry-adapted change of basis."

### Group Theory of Molecular Vibrations

Point-group symmetry determines how many distinct modes exist and whether they appear in infrared, Raman, or neither. This is one of the most direct places in the atlas where character tables and irreducible representations convert immediately into experimentally visible consequences.

The basic workflow is:

1. Identify the molecular point group.
2. Build the reducible displacement representation.
3. Subtract translations and rotations.
4. Decompose into irreducible vibrational species.
5. Check whether those species transform like dipole components or quadratic forms.

That leads directly to the activity rules:

- IR active if the mode transforms like `x`, `y`, or `z`
- Raman active if the mode transforms like `x^2`, `y^2`, `z^2`, `xy`, `xz`, or `yz`

This is why CO2 and H2O behave so differently spectroscopically. An inversion center enforces mutual exclusion; without one, modes can be active in both channels.

A useful concrete example is that in linear molecules with inversion symmetry, gerade modes are Raman-active and ungerade modes are IR-active, with mutual exclusion between the two channels. That one rule already explains why symmetry gives some molecules a clean greenhouse-active vibrational structure while leaving others spectroscopically quiet in the infrared.

### Anharmonicity and Fermi Resonance

Real molecules do not remain perfectly harmonic. Anharmonic corrections shift level spacings, permit overtone structure, and create resonant mixing between nearby modes, which is why realistic spectra carry richer structure than the ideal oscillator model predicts.

The Morse potential is the canonical first correction because it captures the asymmetry between compression and dissociation. Real level spacing therefore decreases as excitation rises instead of remaining perfectly uniform.

Fermi resonance then appears when two vibrational states of the same symmetry lie close in energy. The result is the vibrational version of level repulsion: mixed states, shifted line positions, and intensity borrowing.

This is one of the most useful places where the atlas ties molecular spectroscopy back to its broader cross-domain logic. Near-degenerate states of the same symmetry do not simply cross; they mix, repel, and exchange character. The molecular spectrum therefore becomes another precise example of the same avoided-crossing and boundary-sensitivity ideas that recur later in solids and critical systems.

### Molecular Rotation and Rotor Structure

Rotational structure adds an angular layer on top of bonding and vibration. Linear, symmetric-top, and asymmetric-top molecules each turn symmetry constraints into distinct spectral organizations, making rotational spectroscopy a direct probe of geometry.

For a linear rigid rotor the leading spectrum is

```text
E_J = B J(J + 1)
```

and the states form the familiar `SO(3)` angular-momentum multiplets. Symmetric tops add a projection quantum number along the molecular axis; asymmetric tops lose that simplification and generate the dense, irregular spectra familiar from real atmospheric molecules like water.

The important atlas point is that rotation is not an optional fine detail layered on top afterward. It is a symmetry sector with its own representation structure and its own selection rules.

The linear/nonlinear counting is worth keeping visible because it is one of the most effective orientation tools in molecular physics:

- linear molecules have `3N - 5` vibrational modes
- nonlinear molecules have `3N - 6`

That is the bookkeeping bridge between geometry and spectroscopy. Once the symmetry class is known, one already knows how many vibrational and rotational sectors must appear before doing detailed computation.

### Vibrational and Rotational Transition Rules

Molecular spectra are governed not only by energies but by whether transitions transform correctly under the molecular symmetry. The atlas uses this to connect microscopic geometry to line visibility, line absence, and the practical logic of spectroscopic identification.

The practical outcome is that some molecules are spectroscopically loud in one channel and quiet in another for symmetry reasons alone. The manuscript uses homonuclear molecules as the clearest example: high symmetry can remove ordinary dipole activity even when the molecule is dynamically rich.

That is also why the greenhouse-gas discussion belongs naturally here. Infrared activity is not an environmental add-on to the molecular story; it is a direct consequence of symmetry and dipole structure.

### The Chemistry Bridge

This is where the note deliberately approaches, but does not collapse into, chemistry. Physics supplies exact statements about orbitals, surfaces, and symmetry; chemistry begins when stable higher-level patterns such as functional groups, reaction classes, and synthetic regularities become the natural units of explanation.

The manuscript's stance is clear: chemistry is not "less exact physics," but a new compression layer. Potential surfaces, orbital structure, and symmetry still constrain everything, yet chemical explanation becomes efficient only when it starts talking about recurring motifs rather than about the full many-electron wavefunction every time.

That is why this note ends at the bridge rather than trying to absorb chemistry completely. Molecular physics prepares the handoff; it does not erase the need for the next map.
## Connections to Other Regions

This region grows directly out of [2 - atomic and optical physics.md](2 - atomic and optical physics.md) and leads into [11 - boundary territories.md](11 - boundary territories.md). It also shares heavy use of symmetry language from [1 - foundations and language.md](1 - foundations and language.md).
