globalVar = "Global Scope"
print("Global Variable called from outside class before class call:",globalVar)
class FirstClass():
    classVar = 10
    print("Global Variable called from inside class:",globalVar)
    #Here self is the instance of the class
    def class_meth(self):
        print("Type is", type(self))
        print("Hello. Method inside Class")
        print("Global Variable called from method inside class:",globalVar)

print("Global Variable called from outside class after class call:",globalVar)
ob = FirstClass()
ob.class_meth()
print("Class Variable:", FirstClass.classVar)