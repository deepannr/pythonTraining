'''
    b - Blue
    k - Black
    c - Cyan
    g - Green
    m - Magenta
    r - Red
    w - White
    y - Yellow
'''

import numpy as np, matplotlib.pyplot as plp

arr = np.arange(2, 6)
plp.plot(arr, 'y', label = 'PowerOne')
plp.plot(arr**2, 'r', label = 'Square')
plp.plot(arr**3, 'k', label = 'Cube')
plp.plot(arr**4, 'b', label = 'PowerFour')
plp.plot(arr*40, 'c', label = 'MultiplyFourty')
plp.legend()
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")
plp.suptitle("Super Title")
plp.title("Title")
plp.grid(True)
plp.show()


plp.plot(arr, '--', label = 'PowerOne')
plp.plot(arr**2, '-.', label = 'Square')
plp.plot(arr**3, '--', label = 'Cube')
plp.plot(arr**4, ':', label = 'PowerFour')
plp.plot(arr*40, '--', label = 'MultiplyFourty')
plp.legend()
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")
plp.suptitle("Super Title")
plp.title("Title")
plp.grid(True)
plp.show()


plp.plot(arr, '*', label = 'PowerOne')
plp.plot(arr**2, 'o', label = 'Square')
plp.plot(arr**3, 'D', label = 'Cube')
plp.plot(arr**4, 's', label = 'PowerFour')
plp.plot(arr*40, '^', label = 'MultiplyFourty')
plp.legend()
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")
plp.suptitle("Super Title")
plp.title("Title")
plp.grid(True)
plp.show()