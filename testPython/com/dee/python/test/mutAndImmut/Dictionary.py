'''
    Dictionary have braces { & }
    Lists have square braces [ & ]
    Tuples have curly braces ( & )
'''

locations = {'city' : ['Kg', 'Hsra', 'Svg'], 'state' : ['TN', 'KL', 'KA']}
print(type(locations))
myDictionary = {'Name' : 'Dee', 'Age' : 39, 'locations' : locations}

tempDict = myDictionary['locations']

print(myDictionary['locations'])
print(myDictionary['Name'])
print(tempDict['city'])
print(tempDict['state'])

print("\n---Copy---")
tmpDict = myDictionary.copy()
print(tmpDict)

print("\n---Keys and Items---")
print(myDictionary.keys())
print(myDictionary.items())

print("\n---Sorting---")
print(sorted(myDictionary.keys()))
print(sorted(myDictionary.items()))


# # Conditional Operator 
print("\n---Present or Not---")
print('Name' in myDictionary)

print('name' not in myDictionary)

print("\n---Remove and Find---")
del(myDictionary['Age'])
print(myDictionary.get("Age"))
print(myDictionary["Name"])
#print(myDictionary["Age"]