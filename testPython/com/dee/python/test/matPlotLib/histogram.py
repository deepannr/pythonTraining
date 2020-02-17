import numpy as np, matplotlib.pyplot as plp

someValue = np.random.randn(10, 10)
np.random.randn(10, 10)
print(someValue)

#Histogram
plp.hist(someValue)
plp.title("Histogram")
plp.suptitle("SuperTitle")
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")
plp.show()