#Exercice 1
numMonth = int(input("Enter the number of the month: "))
if numMonth >= 3 and numMonth <= 5:
    print("Spring")
elif numMonth >= 6 and numMonth <= 8:
    print("Summer")
elif numMonth >= 9 and numMonth <= 11:
    print("Autumn")
else:
    print("Winter")

#Exercice 2
for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#Exercice 3
name = input("Enter your name: ")
my_name = "Gilles"
while name != my_name:
    print("Wrong name, try again.")
    name = input("Enter your name: ")

#Exercice 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']


#Exercice 5
a = int(input("Entrez le premier nombre : "))
b = int(input("Entrez le deuxième nombre : "))
c = int(input("Entrez le troisième nombre : "))

print(f"Le plus grand nombre est : {max(a, b, c)}")


#Exercice 6
import random

while True:
    nombre_utilisateur = int(input("Devinez un nombre entre 1 et 9 : "))
    if 1 <= nombre_utilisateur <= 9:
        break
    else:
        print("Nombre invalide ! Veuillez entrer un nombre entre 1 et 9.")

nombre_aleatoire = random.randint(1, 9)

print(f"Le nombre aléatoire était : {nombre_aleatoire}")

if nombre_utilisateur == nombre_aleatoire:
    print("🎉 Gagnant !")
else:
    print("😔 Meilleure chance la prochaine fois !")