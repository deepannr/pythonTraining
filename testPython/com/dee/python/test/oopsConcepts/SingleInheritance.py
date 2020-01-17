class BaseClass():
    def oneMethod(self):
        print("Base Class Method")
        
class DerivedClass(BaseClass):
    pass

class SubClass(BaseClass):
    def oneMethod(self):
        print("Derived Class Method")

base = BaseClass()
derv = DerivedClass()
subs = SubClass()

print("---Base Class---")
base.oneMethod()
print("\n---Derived Class---")
derv.oneMethod()
print("\n---Sub Class---")
subs.oneMethod()