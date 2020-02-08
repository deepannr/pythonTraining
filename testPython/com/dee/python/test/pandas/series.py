import numpy as np, pandas as pd

arrInt = np.array([5, 212, -9, 342, 1, 505])
pdIntSeries = pd.Series(arrInt)
print("Integer Series:\n", pdIntSeries)

arrFlo = np.array([3.4, 4.0, 4, 3.99, 0.15])
pdFloSeries = pd.Series(arrFlo)
print("Float Series:\n", pdFloSeries)

arrAlp = np.array(['a', 'x', 'b', 'c'])
pdAlpSeries = pd.Series(arrAlp)
print("Alphabet Series:\n", pdAlpSeries)


anoArrAlp = np.array(["a", "x", "b", "c"])
pdAnoAlpSeries = pd.Series(anoArrAlp)
print("Alphabet Series:\n", pdAnoAlpSeries)

dictAssign = {'a' : 1, 'b' : 2, 'z': 26, 's': 2026, 'd': 2620, 'j': 25}
pdDict = pd.Series(dictAssign)
print("-Assign Index:\n", pdDict)
print("Slicing (2 to 4):\n", pdDict[2:4])
print("Sicing even index not present:\n", pdDict[:10])