import qamuy.chemistry as qy
from qamuy.client import Client
from qamuy.utils.file_io import save_job
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

# You can fill in your e-mail address and password.
client = Client(email_address="ryzhou@live.unc.edu", password="rEKv3012")

input = qy.QamuyChemistryInput()
ps = input.target_periodic_system
# see also https://sunqm.github.io/pyscf/modules/pbc/gto.html
#BOHR = 0.529 # unit: angstrom
#unitcell_x = 4. * BOHR
#unitcell_yz = 1.
atoms = ["C","C","H","H","C","C","H", "H"]
coords = [
[-0.617 ,  -0.32662 , 0.0 ],
[ 0.617 ,  0.32662 ,  0.0  ],
[ 0.617  , 1.40362   ,0.0],
[ -0.617   ,-1.40362 , 0.0 ],
[ 1.852 ,      -0.32662 , 0.0 ],
[ 3.086  ,   0.32662,  0.0 ],
[ 3.086  ,   1.40362,  0.0 ],
[ 1.852 ,      -1.40362 , 0.0],
]
lattice_vec = [[ 4.938, 0., 0.], [0.,10, 0.], [0., 0., 10]]
kpt_grid_shape = [1, 1, 1] # number of k-points in each direction.
dimension = 1

ps.geometry = qy.periodic_system_geometry(atoms, coords, lattice_vec, kpt_grid_shape)
ps.geometry.dimension = dimension
ps.basis = "ccpvdz"
ps.num_excited_states = 0
ps.multiplicity = 1  # required (from ver. 0.18.1)

# CAS
ps.cas = qy.cas(4, 4)
input.solver.type = "VQE"

input.ansatz.type = "HARDWARE_EFFICIENT"
input.ansatz.depth = 6
input.ansatz.is_state_real = True
input.ansatz.reference_state = "RHF"
input.ansatz.trotter_steps = 4
input.ansatz.use_random_initial_guess=True
#input.ansatz.randomness_type= "GAUSSIAN"
input.ansatz.spin_adapted_ref_state = True
#input.ansatz.randomness_variance = 0.5
input.ansatz.init_param_random_seed = 1

input.optimizer.type = "BFGS"
input.optimizer.gtol = 1e-6
input.cost_function.s2_number_weight= 100000.
input.cost_function.sz_number_weight= 100000.
input.cost_function.particle_number_weight= 100000.
# exact simulator (state vector)

input.cost_function.type = "SIMPLE"

# exact simulator (state vector)
input.quantum_device.type = "EXACT_SIMULATOR"


job=client.submit(input)
save_job(job, filename="cas44.json")
results = client.wait_and_get_job_results([job])
print (results[0].output)
