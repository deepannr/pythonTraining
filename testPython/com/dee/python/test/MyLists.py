'''
    Lists have square braces [ & ]
    Tuples have curly braces ( & )
'''

myList = [1, 1.1, "String"]

print(myList)

'''
List even can contain list inside and tuples also
'''

modifiedList = [myList, "Basic", (0, 2, 4)]

print(modifiedList)
print(modifiedList[0])
print(modifiedList[0][2])
print(modifiedList[1])
print(modifiedList[2][2])