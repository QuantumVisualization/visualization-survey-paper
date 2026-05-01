"""Generate Q Sphere visualization figures for the survey paper."""
import os
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere

# Ensure figures_main directory exists
os.makedirs("figures_main", exist_ok=True)

# Figure 1: 2-qubit Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)
state1 = Statevector(qc1)
fig1 = plot_state_qsphere(state1, show_state_labels=True, show_state_phases=True, use_degrees=True)
fig1.savefig("figures_main/qsphere-bell.png", dpi=150, bbox_inches="tight")
plt.close(fig1)

# Figure 2: 3-qubit GHZ state |GHZ₃⟩ = (|000⟩ + |111⟩)/√2
qc2 = QuantumCircuit(3)
qc2.h(0)
qc2.cx(0, 1)
qc2.cx(1, 2)
state2 = Statevector(qc2)
fig2 = plot_state_qsphere(state2, show_state_labels=True, show_state_phases=True, use_degrees=True)
fig2.savefig("figures_main/qsphere-ghz.png", dpi=150, bbox_inches="tight")
plt.close(fig2)

print("Q Sphere figures generated successfully.")
