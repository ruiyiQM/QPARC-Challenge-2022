n=3
length= 2.469 
x1= 0.58442
x2=-0.58442


w=open(str(n)+".in","w")
w.write("lattice_vector\t"+ str(2.469*n)+"\t0.0 0.0\n")
w.write("lattice_vector 0.0 50 0.0\n")
w.write("lattice_vector 0.0 0.0 50.0\n")
for i in range(0,n):
   w.write("atom\t"+str(-0.58442+2.469*i)+"\t -0.32662  0.0    C\n")
   w.write("atom\t"+str(0.58442+2.469*i)+"\t   0.32662  0.0    C\n")
   w.write("atom\t"+str(0.58442+2.469*i)+"\t   1.40362  0.0    H\n")
   w.write("atom\t"+str(-0.58442+2.469*i)+"\t -1.40362  0.0    H\n")
