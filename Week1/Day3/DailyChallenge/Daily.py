class farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        
        print(f"\n{self.name}\n")
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")
        print(f"\nE-I-E-I-0!")
        print(f"\n  Total animaux   : {sum(self.animals.values())}")
    
    def get_animal_types(self):
        return list(self.animals.keys())
    
    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_list = [f"{animal}s" if self.animals[animal] > 1 else animal 
                       for animal in animal_types
                       ]
        if len(animal_list) == 1:
            animal_string = animal_list[0]
        else:
            animal_string = ", ".join(animal_list[:-1]) + f" and {animal_list[-1]}"
            return f"The farm {self.name} have {animal_string}."
    

macdonald = farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())