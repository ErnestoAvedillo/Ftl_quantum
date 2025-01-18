from qiskit_ibm_runtime import QiskitRuntimeService
from settings import MY_API_TOKEN

QiskitRuntimeService.save_account(
    channel='ibm_quantum',
    token=MY_API_TOKEN,  # Replace with your actual token
    url='https://auth.quantum-computing.ibm.com/api',  # Optional, defaults to public URL
    overwrite=True  # Set to True to overwrite existing credentials
)

from qiskit import Aer
similators = Aer.backend()
for sim in simulators:
    print(sim)
"""
    method="matrix_product_state",
    matrix_product_state_max_bond_dimension=200,
    matrix_product_state_truncation_threshold=1e-6,
    mps_log_data=True,
)"""
from qiskit_aer import AerSimulator
simulators = AerSimulator()
print(simulators.available_methods())
print(simulators.available_devices())

#from qiskit_ibm_provider import IBMProvider
#backend = IBMProvider().backends.ibm_qasm_simulator    
#print(backend)
# List all available backends
#backends = Aer.backends()

# Filter out simulators (by checking if the backend is a simulator type)
#simulators = [backend for backend in backends if 'simulator' in backend.name()]
#print("Available simulators:")
#for simulator in simulators:
#    print(simulator.name())

#from qiskit.circuit import QuantumCircuit, pauli_twirl_2q_gates
#from qiskit.circuit.library import grover_operator
# 
#oracle = QuantumCircuit(2)
#oracle.z(0)  # good state = first qubit is |1>
#grover_op = grover_operator(oracle, insert_barriers=True)
#grover_op.draw('mpl', filename='grover_circuit.png')
#
#
# 
#qc = QuantumCircuit(2)
#qc.cx(0, 1)
#twirled_circuit = pauli_twirl_2q_gates(qc, seed=123456)
#twirled_circuit.draw("mpl")
