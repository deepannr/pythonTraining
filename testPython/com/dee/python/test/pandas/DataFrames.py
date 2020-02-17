import pandas as pd

oneDList = [10, 20, 30, 40]
oneDTable = pd.DataFrame(oneDList)
print("Default Column Name:\n", oneDTable)

oneDTableIndex = pd.DataFrame({"ColName" : oneDList})
print("With Column Name:\n", oneDTableIndex)

withColNameAndRow = pd.Series(oneDList, index = ["r1", "r2", "r3", "r4"])
print("With Column and Row Name:\n", withColNameAndRow)

dict_var = [{'col1' : 1, 'col2': 2}, {'col1' : 20, 'col2' : 26, 'col3' : 71}, {'col1' : 50, 'col3' : 51}]
dFrameDict = pd.DataFrame(dict_var, index=['row1', 'row2', 'row3'])
print(dFrameDict)

stud1 = pd.Series([90, 95, 99], index=['Physics', 'Chemistry', 'Mathematics'])
stud2 = pd.Series([95, 98, 100, 100], index=['Physics', 'Chemistry', 'Mathematics', 'Cse'])
marksTable = pd.DataFrame({
    "Dee" : stud1,
    "Pan" : stud2 
    })
marksTable['Dp'] = pd.Series([90, 89, 95], index=['Cse', 'Chemistry', 'Mathematics'])

print("Panda stud1 series:\n", stud1)
print("\nPanda stud2 series:\n", stud2)

print("\n---Print All Marks---\n", marksTable)
addRow = pd.DataFrame([[70, 71, 73]], columns=['Dee', 'Dp', 'Pan'])

print("Type of addRow:", type(addRow))
print("Type of stud2:", type(stud2))

print("\n---Add New Row---")
marksTable = marksTable.append(addRow)
print(marksTable)

print("\n---Print Mathematics Row---\n", marksTable.loc['Mathematics'])

print("\n---Print 0th Row---\n", marksTable.iloc[0])

#del and pop is for removing columns
#drop is for removing rows

del(marksTable['Dp'])

print("\n---After removing Dp---\n", marksTable)

delEntry = marksTable.pop('Pan')
print("\n---Popping Pan Entry---\n", delEntry)
print("\n---After removing Pan---\n", marksTable)

marksTable = marksTable.drop(0)
print("\n---After Drop 0---\n", marksTable)


marksTable = marksTable.drop('Chemistry')
print("\n---After Drop Chemistry---\n", marksTable)