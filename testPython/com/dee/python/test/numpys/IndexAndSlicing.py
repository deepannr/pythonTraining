import numpy as np

npArray = np.arange(1, 27)
indexNum = npArray[19]
print("npArray:", npArray)
print("Index(19):", indexNum, " Type Of npArray:", type(npArray), " Type Of Index:", type(indexNum))
indexNumAdd = indexNum + 6
print("Index Addition:", indexNumAdd, " Type:", type(indexNumAdd))

#print(npArray.slice(1, 12, 4))
