import numpy as np

arrMd = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np.savetxt("numpyFile.txt", arrMd)

anothArr = np.loadtxt("numpyFile.txt")
print("anothArr:", anothArr)

np.savetxt("numpyFile.csv", arrMd, delimiter=",")

np.savetxt("numpyFileDelimiter.txt", arrMd, delimiter = ";")

newArr = np.genfromtxt("numpyFileDelimiter.txt", delimiter = ";")

print("From txt:", newArr)