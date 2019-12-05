Str = "Deepan"

print("---- Continue ----")
# if the condition satisfies, skip that and iterate to next
for i in Str:
    if i == "e" or i == "p":
        continue
    print(i)
    
print("---- Break ----")
# Skip if the condition satisfies
for i in Str:
    if i == "e":
        break;
    print(i)
    
print("---- Pass ----")
# Don't want to execute any
for i in Str:
    pass
print (i)

print("\n---- Another Pass ----")
# Here if i = 2 then only allow to pass to next condition 
for i in [1,2,3,4,5]:
    if (i == 2):
        pass
        print(i)