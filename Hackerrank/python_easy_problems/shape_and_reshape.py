import numpy

input_line = input()
str_numbers = input_line.split()
# numbers are entered as strings; we need to convert them to integers
L = list(map(int, str_numbers))
arr = numpy.array(L)
# print(arr)
print(numpy.reshape(arr,(3,3)))