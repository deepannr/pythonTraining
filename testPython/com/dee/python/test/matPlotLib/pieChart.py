import matplotlib.pyplot as plp

pieValue = [20, 71, 26]
pieLabel = ["Me", "All", "SS"]
plp.figure(figsize=(3, 3)) #Size of the plot in inches

plp.pie(pieValue, labels = pieLabel)
plp.title("Pie-Chart")
plp.suptitle("Title")
plp.show()