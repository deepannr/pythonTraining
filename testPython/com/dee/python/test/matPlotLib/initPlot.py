import matplotlib.pyplot as  plt, numpy as np

#plot does in y-axis where x-axis in 0 to n-1
plt.plot([1, 2, 3, 4, 6])
plt.show()


deeRange = range(5)
plt.plot(deeRange)
plt.show()

xAxis = [3, 6, 9, 12, 15]
yAxis = range(5)
plt.plot(xAxis, yAxis)
plt.show()

xValue = range(6)
plt.plot(xValue, [i**2 for i in xValue])
plt.show()

#Plotting square range till 7 in x axis and range in y axis
yValue = range(7)
plt.plot([i**2 for i in yValue], yValue)
plt.show()

#Plotting numpy array from 3 to 16 in steps of 2 in x axis and square in y axis
npArray = np.arange(3, 16, 2)
plt.plot(npArray, [i**2 for i in npArray])
plt.show()