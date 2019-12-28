myList = ["zeroth", "first", "second" , "third", "fourth"]

print("---Last Element---")
print(myList[-1])

print("\n---Last But One Element---")
print(myList[-2])

print("\n--Some Operations---")
print(myList[1-2]) #Last Element same as myList[-1]
print(myList[3-2]) #Second Element same as myList[1]

print("\n---Repetition---")
print(myList * 3)

print("\n---Slicing---")
print(myList[1:3])

print("\n---More Slicing---")
listTuple = ["1st", "2nd", ("1stTup", "2ndTup", "3rdTup", "4thTup"), "3rd"]
print(listTuple[2][1:3])
listTuple = ["1st", "2nd", ("1stTup", "2ndTup", "3rdTup", ["A", "B", "C", "D", "E"], "4thTup"), "3rd"]
print(listTuple[2][3][1:4])

print("\n---Concatenation---")
print(myList + ["fifth", "sixth"])

print("\n---Indexing---")
print(myList[3])
print("second" in myList, "seventh" in myList)

#Both Pop and remove does same operation but pop prints the removed element but remove doesn't
print("\n---Pop---")
print(myList.pop(2))
print(myList)

print("\n---Pop Last Element---")
myList = ["zeroth", "first", "second" , "third", "fourth"]
print(myList.pop())
print(myList)

myList = ["zeroth", "first", "second" , "third", "fourth"]
print("\n---Remove---")
print(myList.remove("first")) 
print(myList)

#Assign will overwrite the existing value but insert will insert in the position provided
print("\n---Insert---")
print(myList.insert(1, "first"))
print(myList)

print("\n---Assign---")
myList[1] = "FirSt"
print(myList)

print("\n---Extend---")
myList = ["zeroth", "first", "second" , "third", "fourth"]
print(myList.extend(["fifth","sixth", "seventh"]))
print(myList)

print("\n---Append---")
print(myList.append("eighth"))
print(myList)

print("\n---Sorted---")
print(sorted(myList))

print("\n---Reverse---")
print(myList[::-1])