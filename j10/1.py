import numpy as np

ar = np.arange(1, 101)
b = ar.reshape(10, 10)
print(b.shape)
print(b)

lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i, end = " ")