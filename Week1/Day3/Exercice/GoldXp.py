#Exercice 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def circumference(self):
        import math
        return 2 * math.pi * self.radius
    
    def print_info(self):
        print(f"Circle with radius: {self.radius}")
        print(f"Area: {self.area()}")
        print(f"Circumference: {self.circumference()}")

circle1 = Circle(5)
circle1.print_info()

#Exercice 2
class MyList:
    def __init__(self, items):
        self.items = items

    def invert(self):
        return self.items[::-1]
    
    def sort(self):
        return sorted(self.items)
    
    def same_length(self, other_list):
        return len(self.items) == len(other_list.items)

list1 = MyList([3, 1, 4, 1, 5])
print(list1.invert())
print(list1.sort())
list2 = MyList([1, 2, 3])
print(list1.same_length(list2))

#Exercice 3
class MenuManager:
    def __init__(self, menu):
        self.menu = [
            {"name": "Soup", "price": 10, "meaning": "B", "gluten_index": False},
            {"name": "Hamburger", "price": 15, "meaning": "A", "gluten_index": True},
            {"name": "Salad", "price": 18, "meaning": "A", "gluten_index": False},
            {"name": "French Fries", "price": 5, "meaning": "C", "gluten_index": False},
            {"name": "Beef bourguignon", "price": 25, "meaning": "B", "gluten_index": True},
            {"meaning" : {"A": "not spicy",
             "B": "a little spicy",
             "C": "very spicy"}
            }
        ]

    def add_item(self, name, price, meaning, gluten_index):
        self.menu.append({"name": name, "price": price, "meaning": meaning, "gluten_index": gluten_index})

    def update_item(self, dish_name, new_price=None, new_meaning=None, new_gluten_index=None):
        for item in self.menu:
            if item["name"] == dish_name:
                if new_price is not None:
                    item["price"] = new_price
                if new_meaning is not None:
                    item["meaning"] = new_meaning
                if new_gluten_index is not None:
                    item["gluten_index"] = new_gluten_index
                break

    def remove_item(self, dish_name):
        self.menu = [item for item in self.menu if item["name"] != dish_name] 
        return self.menu

menu_manager = MenuManager([])
menu_manager.add_item("Pizza", 12, "A", True)
menu_manager.add_item("Pasta", 14, "B", False)
print(menu_manager.menu)