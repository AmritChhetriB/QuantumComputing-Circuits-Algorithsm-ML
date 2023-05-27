# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Circuit Design
# Module: Cirq, https://pypi.org/project/qiskit/
# Installations: pip install qiskit or using Interpreter option in PyCharm

from qiskit import *
cirq= QuantumCircuit(3,3)

cirq.h(0)
cirq.cx(0,1)
cirq.cx(0,2)
#cirq.draw('mpl')
#Displays in Jupypter Notebook

