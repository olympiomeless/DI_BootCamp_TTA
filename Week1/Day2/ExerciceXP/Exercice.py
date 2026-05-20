#Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = dict(zip(keys, values))
print(my_dict)

#Exercice 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
sum = 0
for key, value in family.items():
    age = family[key]
    if age > 12 :
        print(f"the ticket for {key} is $15")
        sum += 15
    elif age >= 3 and age <= 12:
        print(f"the ticket for {key} is $10")
        sum += 10
    else:
        print(f"the ticket for {key} is free")
        sum += 0
print(f"The total cost for the family is {sum} dollars")

#Exercice 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": "pink, green"
    }
}

brand.update({"number_stores": 2})  

print(f"Zara's clients are {brand['type_of_clothes']}")

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

brand.pop("creation_date")

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

#Exercice 4
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exercice 5
import random
def get_random_number(num):
    a = random.randint(1, 100)
    if num == a:
        return print("Congratulations! You guessed the number!")
    else:
        print("This number is not supported: " + str(num) + "and the random number is " + str(a))

get_random_number(50)

#Exercice 6
def make_shirt(size="large", text="I love Python"):
    print(f"The shirt is size '{size}' and says: '{text}'")

make_shirt()

make_shirt(size="medium")

make_shirt(size="small", text="Python is awesome!")

make_shirt(size="small", text="Hello!")

#Exercice 7
def get_random_temp():
    return random.randint(-10, 40) 

def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that\’s freezing! Wear some extra layers today.")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don\’t forget your coat.")
    elif temp >= 16 and temp < 23:
        print("Nice weather.")
    elif temp >= 23 and temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It\’s really hot! Stay cool.")

#Exercice 8
toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("\n--- Your Pizza List Order ---")
if toppings:
    print("Toppings:")
    for t in toppings:
        print(f"  - {t}")
else:
    print("No toppings added.")

total = base_price + (len(toppings) * topping_price)
print(f"\nBase price        : ${base_price:.2f}")
print(f"Toppings ({len(toppings)}x$2.50) : ${len(toppings) * topping_price:.2f}")
print(f"Total cost        : ${total:.2f}")