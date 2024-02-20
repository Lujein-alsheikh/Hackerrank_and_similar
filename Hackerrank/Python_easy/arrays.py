import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, float)
    reversed_arr = arr[::-1].astype(float)
    return reversed_arr
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)