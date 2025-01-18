from qiskit_ibm_runtime import QiskitRuntimeService

MY_API_TOKEN = "dc09a3509c7c08a114cb746820482602d4d734ffd823c7452474d91374bddd84eeb579213a440882e0fc14e7a1ba2c0f45e663a7e52145c5b01862de30bcd6af"
QiskitRuntimeService.save_account(
    channel='ibm_quantum',
    token=MY_API_TOKEN,  # Replace with your actual token
    url='https://auth.quantum-computing.ibm.com/api',  # Optional, defaults to public URL
    overwrite=True  # Set to True to overwrite existing credentials
)

from qiskit_aer import AerSimulator
simulator = AerSimulator()
"""
    method="matrix_product_state",
    matrix_product_state_max_bond_dimension=200,
    matrix_product_state_truncation_threshold=1e-6,
    mps_log_data=True,
)"""
print(simulator.available_methods())
print(simulator.available_devices())

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
