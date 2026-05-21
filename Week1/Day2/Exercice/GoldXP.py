#Exercice 1 & 2
birthdays = {
    "Orlane": "2005/07/20",
    "Gilles": "2000/10/18",
    "Maelys": "2024/05/18",
    "Paule": "2003/07/19",
    "Emmanuella": "2009/01/07"
}

print("Welcome to the birthday dictionary!")
print("You can look up the birthdays of the people in the list!")
print("Here are the people in the list:")
for name in birthdays:
    print(f"- {name}")

name = input("Enter the name of the person whose birthday you want to know: ")

if name in birthdays:
    birthday = birthdays[name]
    print(f"{name}'s birthday is on {birthday}.")
else:    
    print(f"Sorry, I don't have the birthday information for {name}.")

#Exercice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("Enter a name to check if it's in the list: ")

if name in names:
    print(f"{name} we should be printing the index {names.index(name)}")
else:
    print(f"{name} is not in the list.")

#Exercice 4
def throw_dice():
    import random
    return random.randint(1, 6)

def throw_until_doubles():
    result1 = throw_dice()
    result2 = throw_dice()
    tuple = (result1, result2)
    while result1 != result2:
        print(f"You rolled a \({tuple.value}\).")
        result1 = throw_dice()
        result2 = throw_dice()
    print(f"You rolled a \({result1} ,{result2}\). You got doubles!")
   
