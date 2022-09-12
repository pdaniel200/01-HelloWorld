print('------- # CLASE -------------------')


class Point:
    def move(self):  # definim metoda move
        print("functia move")

    def draw(self):  # definim metoda draw
        print("functia draw")


point1 = Point()  # cream un obiect si il accesam ca pe o functie, totul atribuit unei variabile
point1.draw()  # folosim metoda dot.method operator ca sa apelam metoda draw definita din clasa
point1.x = 10  # attributes
point1.y = 20
print((point1.x))
print((point1.y))

point2 = Point()
point2.move()
point2.aaa = 44
print((point2.aaa))

print('------- # CONSTRUCTORS -------------------')


# A CONSTRUCTOR IS A FUNCTION THAT GETS CALLED AT THE TIME WHEN CREATING AN OBJECT

class Point:
    def __init__(self, x, y):
        self.x = x  # setam atributul x <self.x este atribut> la argumentul x
        self.y = y

    def move(self):
        print("functia move")

    def draw(self):
        print("functia draw")


print('------- # CONSTRUCTORS  exercitiu-------------------')


class Person:
    def __init__(self, name):
        self.name = name  # self se refera la obiectul curent, setam name attribute de la obiectul curent, la name argument pasat in aceasta metoda

    def talk(self):  # definim metoda talk
        print(f'Hi, I am {self.name}')


john = Person('John Smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()

print('------- # INHERRITANCE -------------------')


class Mamal:
    def walk(self):
        print('walk method')


class Dog(Mamal):
    def bark(self):
        print('bark method')


class Cat:
    def meow(self):
        print('meow method')


class Monkey(Mamal):
    pass


rexi = Dog()
rexi.bark()
rexi.walk()

mitzii = Cat()
mitzii.meow()

maimutza = Monkey()
maimutza.walk()

print('------- # MODULES -------------------')

import modul_1 # importa tot fisierul modul1.py
print(modul_1.kg_to_lbs(70))

from modul_1 import kg_to_lbs
print(kg_to_lbs(70))