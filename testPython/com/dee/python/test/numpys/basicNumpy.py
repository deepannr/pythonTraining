import numpy as np

singleDimArray = [1, 2, 3]
numpyArray = np.array(singleDimArray)

print("---Single Dimension Array---")
print(singleDimArray, type(singleDimArray))
print(numpyArray, type(numpyArray))
print(np.arange(-10, 10))
print(np.zeros((3, 4))) #Forms 3 rows x 4 columns multi dimensional zero array
print(np.linspace(6, 24, 4)) #Splitting 6 to 24 into 4 parts
print(np.linspace(0, 60, 11)) #Splitting 0 to 60 into 11 parts


twoDimArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numpyMultiArray = np.array(twoDimArray)
print("\n---Two and Multi Dimension Array---")
print(twoDimArray, type(twoDimArray))
print(numpyMultiArray, type(numpyMultiArray))

mArray = np.zeros(8)
arr3d = mArray.reshape(2,2,2)
mRavel = arr3d.ravel()
print("2x2x2:", arr3d) #3 Dimensional Array
print("Ravel:", mRavel)
print("4x2:", mArray.reshape(4,2))
print("8x1:", mArray.reshape(8,1))

print("\n---Unorganized Array---")
print(np.array([[1, 2, 3], [4, 5]]))