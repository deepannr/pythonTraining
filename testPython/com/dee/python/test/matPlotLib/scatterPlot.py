import matplotlib.pyplot as plp, numpy

xValue = numpy.random.randn(50)
yValue = numpy.random.randn(50)

plp.scatter(xValue, yValue)
plp.title("Scatter Plot")
plp.suptitle("Scatter Title")
plp.grid(True)
plp.xlabel("xLabel")
plp.ylabel("yLabel")
plp.show()