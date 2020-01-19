try:
    print(9/1)
    print(10/0)

except ZeroDivisionError:
    print("Zero Divide")

else:
    print("No exception")