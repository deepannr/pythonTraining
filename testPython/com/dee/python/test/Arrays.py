arrays = []

arrays.append('Dee')
arrays.append(20)
print(arrays)

arrays.append("15")
arrays.append("One")
arrays.append("15")
arrays.append('3')
arrays.append(15)
arrays.insert(0, 1)
print(arrays)

# Remove first Occurrence of String 15
arrays.remove("15")
print(arrays)

# Removing 3rd Element
del arrays[3]
print(arrays)
