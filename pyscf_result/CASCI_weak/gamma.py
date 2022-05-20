#!/usr/bin/env python
#
# Author: Xiao Wang <xiaowang314159@gmail.com>
#
"""
This example first runs a closed-shell periodic EOM-EE-CCSD with K-point
sampling, a.k.a. EOM-EE-KRCCSD, for singlet excited states on one of the
three provided systems.
Then a molecular EOM-EE-RCCSD based on Gamma-point Hartree-Fock is done, where
a supercell (unit cell with its nmp replicas) is used.
Excitation energies from the two sets of calculations should match.
"""

import numpy as np
from pyscf import gto, scf, cc
from pyscf.cc import eom_rccsd as mol_eom_rccsd
from pyscf.pbc import gto, scf, cc
from pyscf.pbc.cc import eom_kccsd_rhf as eom_krccsd
from pyscf.pbc.tools.pbc import super_cell
from pyscf.cc.rccsd import RCCSD

from pyscf import mcscf
cell = gto.Cell()
cell.verbose = 7
cell.max_memory = 80000  # MB

#
# Helium crystal
#
cell.atom = '''
C -0.58442   -0.32662  0.0    
C  0.58442   0.32662   0.0    
H  0.58442   1.40362   0.0    
H -0.58442   -1.40362  0.0    
C  1.8845799999999997       -0.32662  0.0    
C  3.05342    0.32662  0.0    
H  3.05342    1.40362  0.0    
H  1.8845799999999997       -1.40362  0.0    
'''
#cell.basis = [[0, (1., 1.)], [0, (.5, 1.)]]
cell.a = '''
4.938000000, 0.0000000000, 0.00000000
0.000000000, 10.000000000, 0.00000000
0.000000000, 0.000000000, 10.000000000
'''

cell.basis = 'cc-pvdz'
cell.build()

nmp = [1,1,1]
nroots_test = 1

# Supercell
scell = super_cell(cell, nmp)

# Gamma-point RHF based on supercell
mf = scf.RHF(scell, exxdiv=None).density_fit()
erhf = mf.kernel()


#mf = scf.addons.convert_to_ghf(mf)
mycas = mcscf.CASCI(mf,6, 6)
mycas.kernel()
mycas.verbose = 4
mycas.analyze()


