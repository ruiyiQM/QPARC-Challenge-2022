
import qamuy.chemistry as qy
from qamuy.client import Client

# You can fill in your e-mail address and password.
client = Client(email_address="ryzhou@live.unc.edu", password="rEKv3012")
setting = qy.QamuyChemistryInput()

# H2O
atoms = ["H", "O", "H"]
coords = [
    [0.968877, 0.012358, 0.000000],
    [-0.019830, -0.025588, 0.000000],
    [-0.229801, 0.941311, 0.000000]
]

molecule = setting.target_molecule
molecule.geometry = qy.molecule_geometry(atoms, coords)
molecule.basis = "6-31g"
molecule.multiplicity = 1
molecule.num_excited_states = 0
molecule.cas = qy.cas(2, 2)

# Electric dipole moment
setting.output_chemical_properties.append(
    qy.output_chemical_property(
        target="dipole_moment", states=[0]
    )
)

setting.post_hf_methods.append(
    qy.PostHFMethod(type="CASCI")
)
setting.mapping.type = "JORDAN_WIGNER"
setting.solver.type = "VQE"

# Set cost function
setting.cost_function.type = "SIMPLE"
setting.cost_function.s2_number_weight = 4.0
setting.cost_function.sz_number_weight = 4.0

setting.ansatz.type = "SYMMETRY_PRESERVING"
setting.ansatz.depth = 4
setting.ansatz.use_random_initial_guess = True
setting.optimizer.type = "BFGS"
setting.quantum_device.type = "EXACT_SIMULATOR"


job = client.submit(setting)
print (job)
results = client.wait_and_get_job_results([job])
output = results[0].output

