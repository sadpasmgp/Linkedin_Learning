

class Animal:
    legs = 4
    tail = 'one'
    def __init__(self):
        pass


class Dog(Animal):
    def __init__(self, genus):
        self.genus = genus
        print(genus)
        print(Animal.legs)

class Cat(Animal):
    def __init__(self, genus):
        self.genus = genus
        print(genus)
        print(Animal.tail)

A = Animal()
D = Dog('Canine')
C = Cat('Feline')

A
D
C