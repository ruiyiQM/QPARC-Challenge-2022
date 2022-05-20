import qamuy.chemistry as qy
import qamuy.plot
from qamuy.client import Client
from qamuy.utils.file_io import save_job
input = qy.QamuyChemistryInput()

# You can fill in your e-mail address and password.
client = Client(email_address="ryzhou@live.unc.edu", password="rEKv3012")
molecule = input.target_molecule
molecule.geometry = qy.molecule_geometry(["H", "H"], [[0.0, 0.0, -0.35], [0.0, 0.0, 0.35]])
molecule.basis = "6-31g"
molecule.multiplicity = 1
molecule.sz_number = 0.0
molecule.num_excited_states = 1  # > 0 for calculating excited states
molecule.cas = qy.cas(2, 2)
# Solver
input.solver.type = "VQD"
# or "SSVQE", "MCVQE"

# Ansatz
input.ansatz.type = "SYMMETRY_PRESERVING"
input.ansatz.depth = 4
# or "HARDWARE_EFFICIENT", "UCCSD", ...

# Optimizer
input.optimizer.type = "BFGS"
# or "SLSQP", "Adam", "NFT", "Powell", ...

# Device
input.quantum_device.type = "EXACT_SIMULATOR"
# or "SAMPLING_SIMULATOR"

# Cost Function
input.cost_function.type="SIMPLE"

# add penalties
input.cost_function.s2_number_weight=10.
input.cost_function.sz_number_weight=10.
input.cost_function.particle_number_weight=10.

# option for VQD
input.cost_function.overlap_weights = [10.]

# Post-HF methods to make a comparison
input.post_hf_methods.append(qy.PostHFMethod(type="CASCI"))
# Chemical properties
properties = input.output_chemical_properties
properties.append(qy.output_chemical_property(target="dipole_moment", states=[0, 1]))
properties.append(qy.output_chemical_property(target="oscillator_strength", state_pairs=[[0, 1]]))
# transition_dipole_moment, gradient, hessian, non_adiabatic_coupling, ...
job = client.submit(input)
save_job(job, filename="job.json")
results = client.wait_and_get_job_results([job])
output = results[0].output
print (output)
print (job)
