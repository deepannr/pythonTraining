a, b = 5, 4
print('--- With Operators ---')
print(a and b)  # Print lesser value
print(a or b)  # Print greater value

print(not b)

print(a is b)
print(a is 5)
print(a is '5')
print(a is not b)

print('\n--- With List ---')
modifiedList = ['myList', 6, "Basic", (0, 2, 4), 'anotherVal']
print(6 in modifiedList)
print('basic' in modifiedList)
print('Basic' in modifiedList)

print('\n--- With Tuple ---')
tempTuple = (0, 2, 4)
modifiedTuple = ('myTuple', 6, "Basic", (0, 2, 4))
print(6 in modifiedTuple)
print('basic' in modifiedTuple)
print('Basic' in modifiedTuple)

print('\n--- Compare Tuple & List ---')
print(modifiedList and modifiedTuple)
print(modifiedList or modifiedTuple)

print(modifiedList in modifiedTuple)
print(tempTuple in modifiedTuple)

print(modifiedList not in modifiedTuple)

print('\n--- With String ---')
today = 'Thursday'
tomorrow = 'Friday'

print(today is 'Thursday')
print(today is tomorrow)
print(today is not tomorrow)

print('\n--- Arithmetic Operations ---')
print(6 / 4)  # 1.5
print(6 // 4)  # 1
print(2 ** 3)  # 2^3
