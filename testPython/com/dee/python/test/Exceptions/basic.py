try:
    print(9/1)
    print(10/0) #If this line is commented else block will execute

except ZeroDivisionError:
    print("Zero Divide")

else:
    print("No exception")

finally:
    print("Always executes")