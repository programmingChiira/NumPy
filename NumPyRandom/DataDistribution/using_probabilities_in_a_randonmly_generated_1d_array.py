import numpy

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)

count3 = numpy.count_nonzero(x == 3)
count5 = numpy.count_nonzero(x == 5)
count7 = numpy.count_nonzero(x == 7)
count9 = numpy.count_nonzero(x == 9)

print(count3)
print(count5)
print(count7)
print(count9)