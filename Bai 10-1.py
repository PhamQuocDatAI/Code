import numpy as np
matrix1 = np.array([(1,2,5), (4,5,7), (7,-3,-5)], dtype = int)
matrix2 = np.array([(2,3,4), (-3,-1,1), (2,-2,4)], dtype = int)
print('Tổng hai ma trận: ',matrix1 + matrix2)
print('Tích hai ma trận: ',matrix1 * matrix2)
print(matrix1.transpose() ,' là ma trận chuyển vị của matrix1') 