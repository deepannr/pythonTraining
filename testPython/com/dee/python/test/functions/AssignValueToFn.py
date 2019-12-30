def math_operations(a, b, c, d):
    print(a, b, c, d)
    return ((a + b) / (c - d))

    
print("\n---Assign value to functions---")
# Here order doesn't matter as we can assign to variables while passing in any order
print(math_operations(4, 3, 2, 1))
print(math_operations(b=4, d=1, a=5, c=2))

print("\n---Default Value---")


def default_val(a, b, c=2):
    print(a, b, c)
    return ((a + b) / c)


# Here if c value is provided then it will take that value else will take the default value
print(default_val(4, 6, 5))
print(default_val(4, 6))

print("\n---Variable Arguments---")
def var_agrs(user, *users):
    print("User 1:", user)
    value = 2
    for var in users:
        print("User %s: %s" % (value, var))
        value += 1


print("One Arg")
var_agrs("One")
print("Two Arg")
var_agrs("One", "Two")
print("Three Arg")
var_agrs("One", "Two", "Three")
print("Four Arg")
var_agrs("One", "Two", "Three", "Four")

print("\n---Variable Arguments with immutable---")
def var_args_immutable(a1, a2, *an, **anotherType):
    print("1st Arg:", a1)
    print("2nd Arg:",a2)
    print("nth Args:",an)
    for aa in an:
        print(aa)
    
    print("Keyword Args:",anotherType)

var_args_immutable(10, 20)
var_args_immutable(10, 20, 30)
var_args_immutable(10, 20, 30, 40)
var_args_immutable(10, 20, 30, 40, name="User", age=20, gender="M")