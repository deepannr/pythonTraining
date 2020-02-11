import pandas as pd

readCsvFile = pd.read_csv("C:/dev/projects/PythonTraining/Code/pythonTraining/testPython/com/dee/python/test/Fastag.csv")
print("---Reading from Fastag.csv File---\n", readCsvFile)
readCsvFile.to_csv("LocalFastag.csv")

readCsvFile.to_excel("LocalFastag.xlsx")
#readXlsFile = pd.read_excel("C:/dev/projects/PythonTraining/Code/pythonTraining/testPython/com/dee/python/test/Jan2020.xlsx")
#print("\n---Reading xls file---\n", readXlsFile)
#readXlsFile.to_excel("LocalJan2020.xls")




#pd.read_