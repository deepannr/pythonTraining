#4:30:00

import pandas as pd

oneDList = [10, 20, 30, 40]
oneDTable = pd.DataFrame(oneDList)
print(oneDTable)

dict_var = [{'col1' : 1, 'col2': 2}, {'col1' : 20, 'col2' : 26, 'col3' : 71}, {'col1' : 50, 'col2' : 51}]
dFrameDict = pd.DataFrame(dict_var, index = ['row1', 'row2', 'row3'])
print(dFrameDict)


stud1 = pd.Series([90, 95, 99], index = ['Physics', 'Chemistry', 'Mathematics'])
stud2 = pd.Series([95, 98, 100, 100], index= ['Physics', 'Chemistry', 'Mathematics', 'Cse'])
marksTable = pd.DataFrame({
    "Dee" : stud1,
    "Pan" : stud2 
    })
marksTable['Dp'] = pd.Series([90, 89, 95], index = ['Cse', 'Chemistry', 'Mathematics'])
print(marksTable)