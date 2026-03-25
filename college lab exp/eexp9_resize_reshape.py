import numpy as np

arr = np.arange(1, 13)

print("Original Array:\n", arr)

reshaped = arr.reshape(3, 4)
print("\nReshaped (3x4):\n", reshaped)

arr.resize(2, 6)
print("\nResized (2x6):\n", arr)