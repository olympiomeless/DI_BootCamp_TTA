import random
from Exercice import Dog

#Exercice 3
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(super().bark())  
        self.trained = True
    
    def play(self, *other_dogs):
        dog_names = ", ".join(dog.name for dog in other_dogs)
        return f"{self.name} is playing with {dog_names}" 
    
    def do_a_trick(self):
        tricks = [
            "does a barrel roll", 
            "stands on his back legs", 
            "shakes your hand", 
            "plays dead"
        ]
        if self.trained:
            return tricks[0]  # Just return the first trick for simplicity
        else:
            print(f"{self.name} {random.choice(tricks)}")
            return f"{self.name} is not trained yet and can't do a trick."
            
# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
dog1 = PetDog("Buddy", 3, 12)
dog2 = PetDog("Rex", 4, 15)
my_dog.train()
my_dog.play(dog1, dog2)
my_dog.do_a_trick()
