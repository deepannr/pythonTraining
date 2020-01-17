class ConsAndDest():
    def __init__(self):
        self.pubVar = "Public Var"
        print("Constructor:", self.pubVar)
        
    @classmethod
    def anotherConstructor(cls, constructorVar):
        cls.constructorVar = constructorVar
        print(constructorVar)

    def __del__(self):
        self.pubVar = None
        print("Destructor:", self.pubVar)

cAndD = ConsAndDest()
#cAndDes = ConsAndDest.ConsAndDest(400)
del cAndD