# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Circuit Design
# Module: Cirq, https://pypi.org/project/qiskit/
# Installations: pip install qiskit or using Interpreter option in PyCharm
# https://quantum-computing.ibm.com/

from qiskit import *
circuit = QuantumCircuit(2 ,2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0,1], [0,1])
backend = BasicAer.get_backend('qasm_simulator')
print(backend)



