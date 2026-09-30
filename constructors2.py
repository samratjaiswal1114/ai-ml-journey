class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"HI , i am {self.name}")


jhon = Person("john smith")
jhon.talk()
