

import qamuy.chemistry as qy
from qamuy.client import Client

from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

# You can fill in your e-mail address and password.
client = Client(email_address="ryzhou@live.unc.edu", password="rEKv3012")
input = qy.QamuyChemistryInput()
ps = input.target_periodic_system
# see also https://sunqm.github.io/pyscf/modules/pbc/gto.html
atoms = ["C","C","H", "H"]

coords = [[-0.58442 , -0.32662 , 0.],[0.58442 , 0.32662 , 0.],[0.58442, 1.40362, 0.0],[-0.58442,-1.40362,0.0]]
lattice_vec = [[2.469000000 , 0., 0.], [0., 25, 0.], [0., 0., 25]]
kpt_grid_shape = [4, 1, 1] # number of k-points in each direction.
dimension = 1

ps.geometry = qy.periodic_system_geometry(atoms, coords, lattice_vec, kpt_grid_shape)
ps.geometry.dimension = dimension

ps.basis = "sto-3g"
ps.num_excited_states = 1
ps.multiplicity = 1  # required (from ver. 0.18.1)

# CAS
ps.cas = qy.cas(2, 2)

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

properties = input.output_chemical_properties
properties.append(qy.output_chemical_property(target="oscillator_strength", state_pairs=[[0, 1]]))

job = client.submit(input)
results = client.wait_and_get_job_results([job])
output = results[0].output
print (output)
