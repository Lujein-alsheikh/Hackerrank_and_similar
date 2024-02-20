import numpy

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)  
      
matrix = numpy.array(matrix)
# print(matrix)


print(numpy.transpose(matrix))
print(matrix.flatten())
