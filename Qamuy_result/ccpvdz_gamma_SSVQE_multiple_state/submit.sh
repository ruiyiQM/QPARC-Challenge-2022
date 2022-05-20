#!/bin/bash
#SBATCH -p debug_queue
#SBATCH --job-name=ensemble_13
#SBATCH --ntasks=44
#SBATCH --time=04:00:00



ulimit -s unlimited
#export I_MPI_PMI_LIBRARY=/lib64/libpmi.so
#srun ../../FHIaims/build/aims.x >PB4F2_rcut_5_10s10p10d10f_no_epc.out
python test_sto_two_gamma_cas44.py  >test_sto_two_gamma_cas44_7.out
#qamuy run  test_sto_three_gamma_cas44.json  
#srun ../../FHIaims/build/aims.x 
#srun ../FHIaims/build/aims.x  > double_proton_rcut_5_new.out   

