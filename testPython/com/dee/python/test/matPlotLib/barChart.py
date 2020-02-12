import matplotlib.pyplot as plp

#Bar Chart
xValue = range(10, 20)
yValue = range(15, 25)
plp.title("Bar Chart")
plp.xlabel("X-Axis")
plp.ylabel("Y-Axis")
plp.bar(xValue, yValue)
plp.show()


myDict = {'Dee' : 20, 'Jai' : 25, 'Sni' : 26, 'All' : 71}
for i, key in enumerate(myDict):
    plp.bar(i, myDict[key])

#For each bar will provide the dictionary key. Here only for 3 names are given so 4th will remain no name
plp.xticks(range(3), myDict.keys()) 

    
plp.show()
    