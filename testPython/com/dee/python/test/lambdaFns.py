print("---Basic Lambda---")
answer = (lambda x:x * x)
print(answer(3))

# Here order doesn't matter as we can assign to variables while passing in any order
math_operation = (lambda a, b, c, d: (a + b) / (c - d))
print(math_operation(4, 3, 2, 1))
print(math_operation(d=1, a=4, c=2, b=3))

print("\n---Map Lambda---")
numerals = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numerals))
cubed = list(map(lambda x: x ** 3, numerals))
print("Squares: ", squared)
print("Cubes: ", cubed)

print("\n---Filter---")
numerals_range = range(-10, 10)
negative = list(filter(lambda x: x < 0, numerals_range))
print(negative)

print("\n---Reduce---")
from _functools import reduce
numerals = [1, 2, 3, 4, 5]
result = reduce(lambda x, y : x * y, numerals)
print(result)

# Reduce is same is below
result = 1
for iteration in numerals:
    result = result * iteration
print(result)
