class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    pass
class Cat(Mammal):
    pass
cat1 = Cat()
cat1.walk()