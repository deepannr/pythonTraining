print("---Reversed---")
for i in reversed([1, 2, 3, 4]):
    print(i)

print("\n---All---")
#Here if all are true then prints true. None, 0 are assumed as false. All other string and numbers as true
print(all([True, 5, 1, 3, 5, "True"])) #True
print(all([1, 3, 5, -1])) #True
print(all([1, None])) #False
print(all([True, 0])) #False

print("\n---Any---")
print(any([False, 0, None, 1]))
print(any([False, 0, None, "Str"]))
print(any([False, 0, None, True]))
print(any([True, 1]))
print(any([False, 0, None]))

print("\n---Enumerate---")
countries = ['IND', 'AUS', 'ENG', 'SA', 'USA']
countryEnum = enumerate(countries)
print(type(countryEnum))
print(list(countryEnum))

countryEnum = enumerate(countries, 26)
print(list(countryEnum))