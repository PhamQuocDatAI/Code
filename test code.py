from sympy import * 
import numpy as np
N = np.random.randint(-10, 10, (3, 4))
print(N)
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 
for x in N:
    for y in M:
        y = x
print(M)
print("Matrix : {} ".format(N)) 
   
# Use sympy.rref() method  
M_rref = M.rref()   
      
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))  


# Tìm hiều thêm về .rref 