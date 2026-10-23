"""Inheritance in Python

Inheritance is an object-oriented programming feature where a new class (the
child or derived class) receives attributes and methods from an existing class
(the parent or base class). It lets you reuse and extend code.

Types of inheritance
--------------------

1. Single inheritance: one child class inherits from one parent class.
2. Multiple inheritance: one child class inherits from multiple parent classes.
3. Multilevel inheritance: a class inherits from a child class, forming a chain.
4. Hierarchical inheritance: multiple child classes inherit from the same parent.
5. Hybrid inheritance: a combination of two or more inheritance types.
"""


print("Single inheritance")


class Animal:
    """Parent class used by the examples below."""

    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    """Dog inherits the speak method from Animal."""


Dog().speak()


print("\nMultiple inheritance")


class Flyer:
    def fly(self):
        print("This animal can fly.")


class Swimmer:
    def swim(self):
        print("This animal can swim.")


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
duck.fly()
duck.swim()


print("\nMultilevel inheritance")


class Mammal(Animal):
    pass


class Puppy(Mammal):
    pass


Puppy().speak()


print("\nHierarchical inheritance")


class Cat(Animal):
    pass


Dog().speak()
Cat().speak()


print("\nHybrid inheritance")


class Pet(Animal, Swimmer):
    pass


pet = Pet()
pet.speak()
pet.swim()
