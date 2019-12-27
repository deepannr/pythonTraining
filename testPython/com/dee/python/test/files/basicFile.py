writeObj = open("dee.txt", "w+")


for i in range (0,10):
    writeObj.write("\nPrint line number")
print(writeObj.name)
print(writeObj.mode)
writeObj.close()




import os
os.remove("dst.txt")
os.rename("dee.txt", "dst.txt")

readObj = open("dst.txt", "r")
print(readObj.name)
print (readObj.mode)
for i in range (0,10):
    print(readObj.read())
readObj.close()

readObj = open("dst.txt", "r")
print(readObj.name)
for i in range (0,10):
    print(readObj.read(5))

readObj.close()