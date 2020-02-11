#4:39:00

import pandas as pd

filesPath = "C:/dev/projects/PythonTraining/Code/pythonTraining/testPython/com/dee/python/test/tutorFiles/"

readCsvFile = pd.read_csv(filesPath + "Fastag.csv")
print("---Reading from Fastag.csv File---\n", readCsvFile)
readCsvFile.to_csv(filesPath + "LocalFastag.csv")

readCsvFile.to_excel(filesPath + "LocalFastag.xlsx")

readXlsFile = pd.read_excel(filesPath + "Jan2020.xlsx")
print("\n---Reading xls file---\n", readXlsFile)
readXlsFile.to_excel(filesPath + "LocalJan2020.xlsx")

readJsonFile = pd.read_json(filesPath + "ci_vantive_network_devices.json")
print("\n---Reading JSON file---\n", readJsonFile)