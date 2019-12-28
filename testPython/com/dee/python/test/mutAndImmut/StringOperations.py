myString = "PythonLearning"
another = 'another'
multiQuotes = """MultiQuotes"""
learning = "Learning"
testCase = "learn"
word = "microscopic organ"
duration = 2
print(type(myString))

print("---Reverse---")
print(myString[::-1])

print("\n---Concat---")
print(myString + multiQuotes)

print("\n---Repeat---")
print(another*2)

print("\n---Last Character---")
print(myString[-1])

print("\n---Last But One Character---")
print(myString[-2])

print("\n--Some Operations---")
print(myString[1-2]) #Last Character same as myString[-1]
print(myString[3-2]) #Second Character same as myString[1]

print("\n---Slicing---")
print(myString[6:11])


print("\n---Find String/Character---")
print(learning in myString, testCase in myString, "L" in myString, "l" in myString)

print("\n---Place Holders---")
print("Doing %s for %d months" % (myString, duration))

print("\n---Caps---")
print(myString.capitalize())

print("\n---Encode---")
print(myString.encode("utf-8", another))

#Works on ASCII Code
print("\n---Max and Min Value---")
print(max(myString), min(myString))

print("\n---Index, Find & Replace---")
print(word.index("o")) #First occurrence of matching value
print(word.find("o"))
# print(word.index("O")) ValueError: substring not found
print(word.find("O")) #Difference between find and index is find will not give error if string not identified
print(word.replace("o", "-e-", 2)) #Here o is replaced with -e- only for 2 occurrences