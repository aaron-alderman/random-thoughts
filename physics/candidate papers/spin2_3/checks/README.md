# Checks

This folder contains validation scripts for the Spin(2,3) programme.

## Contents

- [check-corpus.ps1](check-corpus.ps1) checks the local corpus for consistency signals and expected structure.
- [check_diii_boundary_bookkeeping.py](check_diii_boundary_bookkeeping.py) prints the reduced `2+1`-dimensional parity/global bookkeeping for the candidate `T1` boundary spectrum.
- [check_auxiliary_projector_casimir_rewrite.py](check_auxiliary_projector_casimir_rewrite.py) checks that the auxiliary projector on `1 (+) 2` equals the Casimir-zero projector `1 - (4/3)C_aux`.
- [check_auxiliary_vacuum_doublet_candidate.py](check_auxiliary_vacuum_doublet_candidate.py) checks the vacuum-plus-single-occupancy candidate `Lambda^0 V (+) Lambda^1 V ~= 1 (+) 2` coming from a fermionic completion of the quaternionic doublet.
- [check_branch_casimir_superselection_candidate.py](check_branch_casimir_superselection_candidate.py) records the superselection rewrite of the physical-subcarrier projector as observable-branch selection on the even line plus minimal total weak-spin selection on the odd line.
- [check_conditional_static_spectrum_closure.py](check_conditional_static_spectrum_closure.py) checks the final conditional package: once the current observable-branch and odd invariant-pairing rules are granted, the reduced one-generation charges are exactly reproduced.
- [check_even_sector_observable_projector_descent.py](check_even_sector_observable_projector_descent.py) records the even-sector refinement that identifies `P_obs P_aux,0` with the reduced observable/readout-sector projector from the ambient scaffold.
- [check_even_line_exotic_branch_obstruction.py](check_even_line_exotic_branch_obstruction.py) checks the complementary `T2` charges on the auxiliary even line and confirms the exotic doublet sector left over by the selected-slot fit.
- [check_full_fock_auxiliary_obstruction.py](check_full_fock_auxiliary_obstruction.py) checks the top-wedge charges in the full fermionic completion and confirms the extra wrong-type weak-doublet sector.
- [check_minimal_physical_subcarrier_candidate.py](check_minimal_physical_subcarrier_candidate.py) checks the operator-defined minimal physical subcarrier and confirms that it keeps the desired SM-like charges while removing the even-line exotic branch.
- [check_odd_sector_epsilon_channel.py](check_odd_sector_epsilon_channel.py) checks that the odd weak-singlet selector is exactly the antisymmetric `epsilon`-channel projector `(1/2)(1 - tau) = 1 - (1/2) C_tot`.
- [check_minimal_right_handed_singlet_candidate.py](check_minimal_right_handed_singlet_candidate.py) checks the minimal extra-doublet singlet candidate and its `Y = a J^{01} + b Q7` fit.
- [check_quaternionic_auxiliary_block_screening.py](check_quaternionic_auxiliary_block_screening.py) checks that the current quaternionic slice `H(u,v)` gives only the irreducible complex `SU(2)` doublet under the natural left action, not the reducible auxiliary block `1 (+) 2`.
- [check_right_handed_completion_screening.py](check_right_handed_completion_screening.py) checks the anomaly target relations and the failure of the naive `T2`-doubled static carrier to realize right-handed completion.
- [check_unified_carrier_hypercharge_test.py](check_unified_carrier_hypercharge_test.py) checks the smallest unified carrier and confirms the neutral-`S_aux` no-go for one global `Y = a J^{01} + b Q7`.
- [check_unified_carrier_projector_fix.py](check_unified_carrier_projector_fix.py) checks the minimal three-term projector enlargement `Y = a J^{01} + b Q7 + c P_aux,0` on the unified carrier.
- [check_w3_sign_correlation.py](check_w3_sign_correlation.py) numerically checks that `W3[q]` and `W3[q^\dagger]` have opposite sign in the current winding convention.

## Use

Run scripts from the Spin(2,3) project root unless the script itself says otherwise.
