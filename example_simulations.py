"""
Tasar Cycle: Example Simulations Suite
Demonstrating practical applications of the Tasar Framework.
"""

from tasar_quantum_core import TasarQuantumCore
import numpy as np

def run_black_hole_information_recovery_sim():
    """
    Scenario 1: Simulating information survival at a singularity interface.
    Based on the SL -> LT phase transition.
    """
    print("\n[Simulation 1: Black Hole Singularity Interface]")
    tasar = TasarQuantumCore()
    
    # Information approaching saturation (SL Phase)
    st_info = 1.0  # Max density in real spacetime
    print(f"Information at ST limit: {st_info}")
    
    # Rotating into the complex matrix (LT Phase)
    lt_info = tasar.shift_to_lt_phase(st_info)
    print(f"Information 'archived' in LT phase (Complex): {lt_info}")
    
    # Recovery via cosmological feedback
    recovered = tasar.recover_to_st_phase(lt_info)
    print(f"Information recovered to Spacetime: {recovered}")

def run_quantum_decoherence_shield_sim():
    """
    Scenario 2: Shielding a qubit from environmental noise using Phase Rotation.
    """
    print("\n[Simulation 2: Quantum Decoherence Shielding]")
    tasar = TasarQuantumCore()
    
    qubit_state = 0.5 + 0.5j
    print(f"Initial Qubit State: {qubit_state}")
    
    # Apply Tasar Shield
    shielded = tasar.shift_to_lt_phase(qubit_state)
    
    # Simulating 'Noise' that only affects the Real Axis
    noisy_shielded = shielded + 0.02  # Minor perturbation
    
    # Recovering the original state
    final_state = tasar.recover_to_st_phase(noisy_shielded)
    print(f"Final State after Shield & Recovery: {final_state}")

def run_lambda_t_threshold_test():
    """
    Scenario 3: Validating the Tasar Constant (Lambda_T) as a switching threshold.
    """
    print("\n[Simulation 3: Lambda_T Threshold Validation]")
    tasar = TasarQuantumCore()
    l_t = tasar.get_tasar_constant()
    
    print(f"Calculated Lambda_T: {l_t} s.K")
    # According to the paper: tau * T >= Lambda_T [cite: 9, 45]
    test_condition = 2.0e-11 # A value exceeding the threshold
    
    if test_condition >= l_t:
        print("Status: Threshold reached. Initiating Representational Transition (ST -> LT).")

if __name__ == "__main__":
    print("--- STARTING TASAR CYCLE SIMULATIONS ---")
    run_black_hole_information_recovery_sim()
    run_quantum_decoherence_shield_sim()
    run_lambda_t_threshold_test()
