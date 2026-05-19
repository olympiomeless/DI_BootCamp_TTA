#Exercice 1
print("Hello world\n" * 4)

#Exercice 2
print((99**3)*8)

#Exercice 3
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
#print("3" > 3) #Error
print("Hello" == "hello\n") #False

#Exercice 4
computer_brand = "HP Victus CoreI7 GeForce RTX"

print("I have a " + computer_brand + " computer")

#Exercice 5
name = "Maké"
age = 26
shoe_size = 45

info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."

print(info)

#Exercice 6
a = 5
b = 3

if a > b:
    print("Hello World")
else:    print("a is not greater than b")

#Exercice 7
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

#Exercice 8
nameCust = str(input("Enter your name: "))
if nameCust != "Gilles-Chris":
    print("Damage, we\'re not the same name")
else :
    print("Oh my God, this is incredible.\n" + "We\'re the same name: " + nameCust)


#Exercice 9
size = int(input("Enter your size: "))

if size > 145:
    print("Oh sorry, you're too tall to ride a horse.")
elif   size < 145:
    print("Oh sorry, you're too short to ride a horse.")
else:    print("Congratulations, you can ride a horse!")