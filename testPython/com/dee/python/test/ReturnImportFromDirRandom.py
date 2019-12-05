print("---- Return ----")


def addition(x, y):
    return (x + y)


print(addition(10, 16))

from math import factorial, sqrt
print("---- Factorial ----")
print(factorial(6))

print("---- Square Root ----")
print(sqrt(576))

print("---- Listing ----")
import random
print (dir(random))

print("---- Print Random From List ----")
array = ["Dee", "Pan", 20, 26, 25, 45, 46, 51, 71, 52]
print(random.choices(array))

print("---- Print Random Numbers ----")
print(random.random() * 100)
