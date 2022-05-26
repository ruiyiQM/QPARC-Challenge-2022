# High-level periodic electronic structure calculation through quantum computing

Team name: UNC Chapel Hill Quantum Chemistry Team

Team member: Ruiyi Zhou

Applied Challenge: Quantum chemistry challenge 

Project description:


In this project, I aim to study electron correlation interaction in trans-polyacetylene using high-level periodic electronic structure calculations on quantum computers.
According to Peierls distortion, electron-correlation effect can be controlled through bond-length alteration. Given a weak correlated geometry, electron correlation energy from variational quantum eigen-solver (VQE) calculation on intermediate-scale quantum devices (NISQ) devices matches with results of RCCSD and CASCI calculation on classical computer. Furthermore, it is demonstrated that RCCSD calculation fails to describe self-interaction effect, whereas VQE succeeds to fix this problem. 
In the end, I will talk about current challenges and difficulties in finding excited states of extended systems. Meanwhile, borrowing the idea from  SCF, I will also propose to design a new quantum algorithm to target excited states around certain energy range . 


# Preliminary Calculation

2 folded Supercell trans-polyactylene 28 electrons

Basis Set: cc-pvdz

Quantum Solver: VQE (GS), SSVQE (ES), VQD(ES)

Classical Computer Result (pyscf): CCSD(GS), CASCI (GS)，EOM-CCSD (ES)



 

