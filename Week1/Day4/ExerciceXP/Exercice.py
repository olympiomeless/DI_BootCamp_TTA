# Exercice 1: Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def walk(self):
        return f"{self.name} is just sitting there"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Classe enfant
class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"

    def walk(self):
        return f"{self.name} walks gracefully and meows loudly"

# Création d'un objet
bengal_obj    = Bengal("Simba", 3)
chartreux_obj = Chartreux("Luna", 5)
siamese_obj   = Siamese("Nala", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)

print("Sara takes her cats for a walk :\n")
sara_pets.walk()

#Exercice 2
from os import name


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} says Woof!"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} wins the fight against {other_dog.name}!"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} wins the fight against {self.name}!"
        else:
            return f"The fight between {self.name} and {other_dog.name} is a tie!"
    
dog1 = Dog("Buddy", 5, 20)
dog2 = Dog("Max", 3, 15)
dog3 = Dog("Charlie", 4, 25)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

#Exercice 4
class Person:
    def __init__(self, first_name, age, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name} is {self.age} years old."
        return f"{self.first_name} is {self.age} years old."
    
    def is_18(self):
        return self.age >= 18
    

class Family:
    def __init__(self, last_name, members = None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def is_family_adult(self):
        return all(member.is_18() for member in self.members)
    
    def born(self, first_name, age):
        new_member = Person(first_name, age, self.last_name)
        self.members.append(new_member)
        return new_member
    
    def check_majority(self):
        for member in self.members:
            if member.is_18():
                print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
            else:
                print(f"Sorry, you are not allowed to go out with your friends.")
    
    def family_presentation(self):
        print(f"Family {self.last_name} :")
        for member in self.members:
            print(member)

# Test Family class
family = Family("Smith")
family.born("Alice", 17)
family.born("Bob", 19)
family.family_presentation()
family.check_majority()

