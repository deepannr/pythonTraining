print("---- Math Functions ----")
import math
print(math.sqrt(64))
print(math.sin(90))
print(math.cos(90))
print(math.tan(89.9999))

# This is importing only one class instead of import javax.*
from math import factorial
print(factorial(10))

print("---- DateTime ----")
import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print("---- Date & Time ----")
from datetime import date, time
print(date.fromtimestamp(999999999))

# Add as Seconds 86400 is 1 day
print(date.fromtimestamp(1000086399))
print(time.hour)
