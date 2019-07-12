Str = "Deepan"

print("---- Continue ----")
for i in Str:
    if i == "e" or i == "p":
        continue
    print(i)
    
print("---- Break ----")
for i in Str:
    if i =="e":
        break;
    print(i)
    
print("---- Break ----")
for i in Str:
    pass
print (i)