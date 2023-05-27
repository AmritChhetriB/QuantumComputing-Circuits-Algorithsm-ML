# Qiskit Machine Learning
# Author: Amrit Chhetri
#Purpose: Estimator Model

from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit import Parameter
from qiskit import QuantumCircuit
from qiskit.utils import algorithm_globals

algorithm_globals.random_seed = 42
params1 = [Parameter("input1"), Parameter("weight1")]
qc1 = QuantumCircuit(1)
qc1.h(0)
qc1.ry(params1[0], 0)
qc1.rx(params1[1], 0)
qc1.draw("mpl") #workd on Jupyter Notebook
from qiskit.quantum_info import SparsePauliOp

observable1 = SparsePauliOp.from_list([("Y" * qc1.num_qubits, 1)])
observable1 = SparsePauliOp.from_list([("Y" * qc1.num_qubits, 1)])

estimator_qnn = EstimatorQNN(
    circuit=qc1, observables=observable1, input_params=[params1[0]], weight_params=[params1[1]]
)
print("Quantum Neural Network:", estimator_qnn)

