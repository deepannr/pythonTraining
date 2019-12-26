'''
    Dictionary have braces { & }
    Lists have square braces [ & ]
    Tuples have curly braces ( & )
'''

locations = {'city' : ['Kg', 'Hsra', 'Svg'], 'state' : ['TN', 'KL', 'KA']}

myDictionary = {'Name' : 'Dee', 'Age' : 39, 'locations' : locations}

tempDict = myDictionary['locations']

print(myDictionary['locations'])

print(tempDict['city'])

# # Conditional Operator 

print('Name' in myDictionary)

print('name' not in myDictionary)
