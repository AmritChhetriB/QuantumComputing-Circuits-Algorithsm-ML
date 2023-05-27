# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Circuit Design
# Module: Cirq, https://pypi.org/project/cirq/
# Installations: pip install cirq or using Interpreter option in PyCharm

import cirq as ciq
import cirq_google as cg
gqubit = ciq.GridQubit(3, 3)
circuit = ciq.Circuit(
    ciq.X(gqubit)**0.5,
    ciq.measure(gqubit, key='m')
)
print("Circuits:", circuit)

gSimukator = ciq.Simulator()
result = gSimukator.run(circuit, repetitions=20)
print("Results:", result)


