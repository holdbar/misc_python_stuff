# -*- coding: utf-8 -*-

class Animal:
    """
    Abstract animal.
    """

    legs = 0
    tail = False
    roar = ""


class Mutator:
    """
    Responsible for breeding.
    """

    def mutate(self):
        self.animal = Animal()


class Cat(Mutator):
    """
    Cat.
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = "Meeeooow!"


class Dog(Mutator):
    """
    Dog.
    """

    def create_legs(self):
        self.animal.legs = 4

    def create_tail(self):
        self.animal.tail = True

    def create_roar(self):
        self.animal.roar = "Bark! Bark!"


class AnimalOwner:
    """
    Owner of the little zoo.
    """

    __mutator = ""
    def set_animal(self, mutator):
        self.__mutator = mutator

    def create_an_animal_for_me(self):
        self.__mutator.mutate()
        self.__mutator.create_legs()
        self.__mutator.create_tail()
        self.__mutator.create_roar()

    def get_animal(self):
        return self.__mutator.animal


c = Cat()
d = Dog()
ao = AnimalOwner()
ao.set_animal(c)
ao.create_an_animal_for_me()
animal = ao.get_animal()
print(animal.roar)

