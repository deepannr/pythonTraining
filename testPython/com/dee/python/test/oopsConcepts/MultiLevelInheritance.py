class Animal(object):
    def walk(self, level):
        print("Animal Walk from:", level)

class Lion(Animal):
    def roar(self, level):
        print("Lion Roar from:", level)

class Calf(Lion):
    def weep(self, level):
        print("Calf Weep from:", level)
        

print("---Last Level---")
calf = Calf()
calf.weep("Third")
calf.roar("Third")
calf.walk("Third")

print("\n---Mid Level---")
lion = Lion()
lion.roar("Second")
lion.walk("Second")

print("\n---Top Level---")
animal = Animal()
animal.walk("First")