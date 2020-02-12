import matplotlib.pyplot as plp, numpy as np


npArray = np.arange(0, 5, 1)
plp.plot(npArray, npArray, 
         npArray, [i-1 for i in npArray],
         [i-1 for i in npArray], npArray)
plp.grid(True) #Grid graph line is shown
plp.show()



plp.plot(npArray, npArray, label='Same')
plp.plot(npArray, [i-1 for i in npArray], label='Y Axis less')
plp.plot([i-1 for i in npArray], npArray, label='X Axis less')
plp.legend()
plp.grid(True)

#Adding Label
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")

#plp.axis([-2, 9, -2, 8]) #Here x-axis will be shown 3 to 10 and y-axis 2 to 11
#Same as of axis like previous commented
plp.xlim([-2, 9])
plp.ylim([-2, 8])

plp.title("Mat Plot Lib")
plp.suptitle("Learning")
plp.savefig("MatPlot.png")
plp.savefig("MatPlot.pdf")
plp.show()