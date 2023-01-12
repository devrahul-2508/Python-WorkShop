import numpy as np
import matplotlib.pyplot as plt

#rank 1 arrays
arr = np.array(
    [1,4,5]
)

print("\n ___________Rank 1 arrays____________ \n")
print(arr)
print("Type of an array: ", type(arr))
print("Shape of an array: ", arr.shape)

arr[1] = 10
print(arr)

#rank 2 arrays
arr2D = np.array([
    arr,
    [1, 2, 3, 4]
])

print("\n ___________Rank 2 arrays___________ \n")
print(arr2D)
print("Shape = ", arr2D.shape)
print("Type = ", type(arr2D))

print("Rows ===>")
print(arr2D[0], type(arr2D[0]))
print(arr2D[1], type(arr2D[1]))

print("Elements of rows 1 ===>")
for i in range(len(arr2D[0])):
    print(arr2D[0][i])

print("Elements of rows 2 ===>")
for i in range(len(arr2D[1])):
    print(arr2D[1][i])

# addition of two matrixes
arrayZeros = np.zeros([3,4])
print("Type of Zeros Array = ", arrayZeros, arrayZeros.shape)

arrayOnes = np.ones([4,5])
print("Type of Ones Array = ", arrayOnes, arrayOnes.shape)

arrayConsts = np.full([3,3], 5)
print("Type of Const Array = ", arrayConsts, arrayConsts.shape)

arrayRandom = np.random.random([4,5])
print("Type of Random Array = ", arrayRandom, arrayRandom.shape)

for i in range(len(arrayConsts)):
    for j in range(len(arrayConsts[i])):
        if(i==j):
            arrayConsts[i][j] = 0

print("Diagonal \n", arrayConsts)

#array sclicing
temp = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

sub_arr = temp[:2, 1:3]
sub_arr2 = temp[1:, 2:]
sub_arr3 = temp[1, :]
sub_arr4 = temp[:, 2]
sub_arr5 = temp[:, 1:2]
sub_arr6 = temp[1:2, :]

print("__________Array sclicing__________")
print(temp)
print("Sub Array \n", sub_arr)
print("Sub Array 2 \n", sub_arr2)
print("Sub Array 3 \n", sub_arr3)
print("Sub Array 4 \n", sub_arr4)
print("Sub Array 5 \n", sub_arr5)
print("Sub Array 6 \n", sub_arr6)

print("___________Condition Array___________")
print([temp > 2])
print(temp[temp > 2])

#Matrix operations
x = np.array([[3,4], [6,7]], dtype=np.float64)
print(x)
print(x.dtype)

y = np.array([[5,4], [7,8]], dtype=np.float64)
print(y, y.dtype)

print("__________Matrix Operations____________")
print("Numpy Elementwise Addition \n", np.add(x,y))
print("Numpy Elementwise substract \n", np.subtract(x,y))
print("Numpy Elementwise multiplication \n", np.multiply(x,y))
print("Numpy Elementwise division \n", np.divide(x,y))
print("Numpy Elementwise square root \n", np.sqrt(x,y))

v = np.array([9,10])
w = np.array([5,6])

print("Dot product \n", v.dot(w))
print("Dot Product 2 \n", x.dot(v))
print("Transposition \n", x.T)
print("Identical Matrix \n", np.multiply(x, x.T))
print("Sum Collumnwise \n", np.sum(x, axis=0))
print("Sum Rwowise \n", np.sum(x, axis=1))


#Broadcasting
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

b = np.array([1,0,1])
c = np.empty_like(a)
for  i in range(len(a)):
    c[i,:] = a[i,:] + b

stack_v = np.tile(b,[3,1])

print("________Broadcasting__________")
print(c)
print(stack_v)
print(a+stack_v)

#Reshape
r = np.array([
    [1,2,3],
    [4,5,6]
])

reshape = np.reshape(r, [3,2])

print("_______Reshape__________")
print(r.shape)
print(reshape.shape)