#Exercice 1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Whiskers", 3)
cat2 = Cat("Mittens", 5)
cat3 = Cat("Shadow", 2)

def find_oldest_cat(cats):
    oldest_cat = cats[0]
    for cat in cats:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat([cat1, cat2, cat3])
print(f"Oldest cat: {oldest_cat.name}, Age: {oldest_cat.age} years old")

#Exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        return print(f"{self.name} goes woof!")
    
    def jump(self):
        return print(f"{self.name} jumps {self.height * 2} cm high!")

david_dog = Dog("Rex", 50)
david_dog.jump()
sarah_dog = Dog("Buddy", 60)
sarah_dog.jump()

def compare_dogs(dog1, dog2):
    if dog1.height > dog2.height:
        return print(f"{dog1.name} is bigger than {dog2.name}.")
    elif dog1.height < dog2.height:
        return print(f"{dog2.name} is bigger than {dog1.name}.")
    else:
        return print(f"{dog1.name} and {dog2.name} are the same height.")

compare_dogs(david_dog, sarah_dog)

#Exercice 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        return print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []
            sorted_animals[first_letter].append(animal)
        for key in sorted_animals:
            sorted_animals[key].sort()
        return print(sorted_animals)
    
    def get_groups(self):
        groups = {}
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return print(groups)

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()