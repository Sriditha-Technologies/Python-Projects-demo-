import numpy as np

#create two matric
matrix_a=([[1,2],[3,4]])
matrix_b=([[2,3],[4,5]])

#Matrix addition
sum_matrix=np.add(matrix_a , matrix_b)

#Matrix multiplication
Product_matrix=np.matmul(matrix_a ,matrix_b)

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("sum of A and B:\n",sum_matrix)
print("product of A and B:\n",Product_matrix)