import numpy as np

array = np.random.randint(low=1, high=100, size=(3,3))
print(array)
sum = np.sum(array)
print("\nsum = ", sum)
print("\nmin = ", np.min(array), " index = ", np.argmin(array))
print("max = ", np.max(array), " index = ", np.argmax(array))

print("\nsorted array = \n", np.sort(array))