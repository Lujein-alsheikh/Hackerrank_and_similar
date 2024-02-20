import numpy

n, m, p = map(int, input().split())

matrix_1 = []
matrix_2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix_1.append(row)
    
for _ in range(m):
    row = list(map(int, input().split()))
    matrix_2.append(row)   


matrix_1 = numpy.array(matrix_1)
# print(matrix_1)

matrix_2 = numpy.array(matrix_2)
# print(matrix_2)

print(numpy.concatenate((matrix_1, matrix_2), axis = 0))   
