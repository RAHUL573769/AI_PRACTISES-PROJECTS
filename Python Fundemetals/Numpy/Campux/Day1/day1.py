import numpy as       np
c=np.array([1,2,3,4,5])
print(c)

matrix = [
    [1,2,3,45,6],
    [1,3,4,5,7]
]

d = np.array(matrix)

print(d)

# 3D Tensor
d = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],

    [
        [7,8,9],
        [10,11,12]
    ]
])

print(d)
print(d.ndim)

# Shape of tensor
print(d.shape)

# 1. What is this structure?

# Think of it like a stack of matrices (layers).

# You have:

# 👉 Layer 1
# 1  2  3
# 4  5  6
# 👉 Layer 2
# 7  8  9
# 10 11 12

# So overall:

# 👉 2 layers
# 👉 each layer has 2 rows
# 👉 each row has 3 columns

# 2. Shape explanation
# print(d.shape)

# Output:

# (2, 2, 3)

# Meaning:

# Value	Meaning
# 2	number of layers (depth)
# 2	rows in each layer
# 3	columns in each row