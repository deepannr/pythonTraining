'''
    Dictionary have braces { & }
    Lists have square braces [ & ]
    Tuples have curly braces ( & )
'''

tempTuple = (1, 2, 3)
print(type(tempTuple))
'''
Printing all the elements in Tuple
'''
print(tempTuple)

# Printing an element in tuple
print(tempTuple[2])

modifiedTuple = (tempTuple, "Basic", (0, 2, 4), [1, 31, "ListBasic"])

print(modifiedTuple)
print(modifiedTuple[0])
print(modifiedTuple[0][2])
print(modifiedTuple[1])
print(modifiedTuple[2][2])
print(modifiedTuple[3])
print(modifiedTuple[3][2])

modifiedTuple[3][2] = "ListModified"
print(modifiedTuple)