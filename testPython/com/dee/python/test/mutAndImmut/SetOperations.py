word = "microscopic organ"
first = {1, 3, 5, 7, 9}
second = {2, 3, 4, 6, 8}

print("---Set---")
print(type(first))
print(set(word)) #prints unique elements. Every time printing order may be different
print("\n---Union and Intersection---")
print(set(first | second)) #Union. Prints unique elements
print(first | second)

print(first & second) #Intersection


print(first - second) #Present in 1st and not in 2nd
print(second- first) #Present in 2nd and not in 1st

set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 4, 6}
set3 = {1, 3, 5, 7}
print("\n---Sub and Super set---")
print(set2.issubset(set1), set3.issubset(set1))
print(set1.issuperset(set2), set1.issuperset(set3))

print("\n---Remove and Discard---")
first.remove(3)
# first.remove(4) Remove with throw error if element not found whereas discard will not throw error
print(first)
second.discard(3)
print(second)
second.discard(1)