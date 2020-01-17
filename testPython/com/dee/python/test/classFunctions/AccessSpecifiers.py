class TestForAccessSpecifiers():
    def __init__(self):
        self.__initPrivateVar = "Private Variable"
        self._initProtectedVar = "Protected Variable"
        self.initPublicVar = "Public Variable"
    
    def publicMethod(self):
        print("Public Method")
        self.__privateVar = "Private Variable"
        self._protectedVar = "Protected Variable"
        self.publicVar = "Public Variable"
    
    def _protectedMethod(self):
        print("Protected Method")
        self.__anotherPrivateVar = "Private Variable"
        self._anotherProtectedVar = "Protected Variable"
        self.anotherPubVar = "protectedMethod Public Variable"
    
    def __privateMethod(self):
        print("Private Method")
        self.__priVar = "privateMethod Private Variable"
        self._protVar = "privateMethod Protected Variable"
        self.pubVar = "privateMethod Public Variable"


print("---Variables---")
test = TestForAccessSpecifiers()
#print(test.__initPrivateVar) This will not work because of private Scope
print(test._initProtectedVar)
print(test.initPublicVar)

print("\n---Methods---")
test._TestForAccessSpecifiers__privateMethod()
#test.__privateMethod() Can't access like this
test._protectedMethod()
test.publicMethod()