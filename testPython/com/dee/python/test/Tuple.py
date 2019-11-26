'''
    Lists have square braces [ & ]
    Tuples have curly braces ( & )
'''

tempTuple = (1,2,3)

'''
Printing all the elements in Tuple
'''
print(tempTuple)

# Printing an element in tuple
print(tempTuple[2])


modifiedList = (tempTuple, "Basic", (0, 2, 4), [1, 31, "Basic"])

print(modifiedList)
print(modifiedList[0])
print(modifiedList[0][2])
print(modifiedList[1])
print(modifiedList[2][2])
print(modifiedList[3])
print(modifiedList[3][2])