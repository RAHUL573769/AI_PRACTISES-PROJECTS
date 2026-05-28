# [1,2,3,4,5,6]

# [[1,2,3,4,56,7],[12,3,4,5,6]]
# # //matrix
# c++

import numpy as np

lists=[1,2,3,4,5,6]
array_1d=np.array(lists)

print(array_1d)

# List vs array

myList=[1,2,3,4,54,6]

# creating array from list

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array: ", arr_1d)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array: ", arr_2d)

arr_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],

    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr_3d)




array_3dNew=[
[
    [1,2,3,4],[
        5,6,7,8
    ]
    ],
[
    [1,2,3,4],[
        7,8,9,10
    ]
]
]