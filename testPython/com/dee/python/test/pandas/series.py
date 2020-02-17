import numpy as np, pandas as pd

arrInt = np.array([5, 212, -9, 342, 1, 505])
pdIntSeries = pd.Series(arrInt)
print("Integer Series:\n", pdIntSeries)

arrFloat = np.array([3.4, 4.0, 4, 3.99, 0.15])
pdFloatSeries = pd.Series(arrFloat)
print("Float Series:\n", pdFloatSeries)

arrAlp = np.array(['a', 'x', 'b', 'c'])
pdAlpSeries = pd.Series(arrAlp)
print("Alphabet Series:\n", pdAlpSeries)

npRangeArr = np.arange(-5, 5)
pdRangeArr = pd.Series(npRangeArr)
print("NP Range array:\n", pdRangeArr)

dictAssign = {'a' : 1, 'b' : 2, 'z': 26, 's': 2026, 'd': 2620, 'j': 25}
pdDict = pd.Series(dictAssign)
print("-Assign Index:\n", pdDict)
print("Slicing (2 to 4):\n", pdDict[2:4])
print("Slicing even index not present:\n", pdDict[:10])