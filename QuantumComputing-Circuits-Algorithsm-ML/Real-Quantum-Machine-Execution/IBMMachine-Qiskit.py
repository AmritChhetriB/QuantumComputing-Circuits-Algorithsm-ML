# Author: Amrit Chhetri, Digital Forensic Researcher
# Purpose: Running on Real-Machine
# Module: Cirq, https://pypi.org/project/qiskit/
# Installations: pip install qiskit or using Interpreter option in PyCharm

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, IBMQ, execute, transpile, Aer, assemble
#from qiskit.tools.monitor import job_monitor
import warnings
warnings.filterwarnings('ignore')

qr = QuantumRegister(5)
cr = ClassicalRegister(5)

circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0])
circuit.x(qr[1])
circuit.ccx(qr[0], qr[1], qr[2])
circuit.cx(qr[0], qr[1])
circuit.measure(qr, cr)

IBMQ.save_account("421d274b036d601145cfa3f18287ff92d8cc3d9f4d8628e865b60d4495fc6bceb3586aed6b0abbae478f17e8ebb5b178ebf66c1bf362c81ef9396813385b5d9f", overwrite=True)
provider = IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
backend = provider.get_backend('ibmq_quito')

mapped_circuit = transpile(circuit, backend=backend)
qobj = assemble(mapped_circuit, backend=backend, shots=1024)

job = backend.run(qobj)

job.status()
print("Job:", job.job_id())
job = provider.get_backend('ibmq_quito').retrieve_job('chovd84pd6rr9jiumr1g')
result = job.result()
counts = result.get_counts()
print("Counts of 00 and 11:", counts)

