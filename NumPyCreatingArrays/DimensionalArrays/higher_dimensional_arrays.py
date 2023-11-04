# An array can have any number of dimensions.

# When the array is created, you can define the number of dimensions by using the ndmin argument.

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)