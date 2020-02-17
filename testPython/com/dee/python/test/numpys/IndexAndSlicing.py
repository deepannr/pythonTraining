import numpy as np

npArray = np.arange(1, 27)
indexNum = npArray[19]
print("---Indexing---")
print("npArray:", npArray, " Type Of npArray:", type(npArray))
print("Index(19):", indexNum, " Type Of Index:", type(indexNum))
indexNumAdd = indexNum + 6
print("Index Addition:", indexNumAdd, " Type:", type(indexNumAdd))
indAdd = indexNum + npArray[5]
print("Another Index Add:", indAdd, "Type:", type(indAdd))
print("Negative Indexing:", npArray[-1], npArray[25], npArray[-26], npArray[0])
# print(npArray.slice(1, 12, 4))


print("\n---Slicing---")
arr_slice = slice(2, 26, 3) 
slice_array = npArray[arr_slice]  # Starts with 2nd index, ends up till 26th index with step of 3 
print("Slicing:", slice_array)
print("Arranging into 2 dimensional:\n", slice_array.reshape(4, 2))
arra3d = slice_array.reshape(2, 2, 2)
print("Arranging into 3 dimensional:\n", arra3d)
print("Shape:", arra3d.shape, "Dimension:", arra3d.ndim, "Items:", arra3d.itemsize)
print("Between Slicing:", npArray[3:20])
print("Before Slicing:", npArray[:20])
print("After Slicing:", npArray[5:])


print("\n---Slicing Multi Dimensional Array--")
print("Row x Column")
arrMd = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("0:2 x 0:2:\n", arrMd[0:2, 0:2])
print("0:5 x 1:2:\n", arrMd[0:5, 1:2])
print(":2 x 1: :\n", arrMd[:2, 1:])

print("\n---Printing random Array---")
print("Int array:", np.empty([3,4], dtype=int))
print("Float Array:", np.empty([3, 2], dtype=float))
print("Byte Array:", np.empty([3, 2], dtype=bytes))