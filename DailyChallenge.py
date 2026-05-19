# Daily Challenge - Challenge 1

def generer_multiples(number, length):
    multiples = []
    for i in range(1, length + 1):
        multiples.append(number * i)
    return multiples

number = int(input("Entrez un nombre : "))
length = int(input("Entrez la longueur de la liste : "))

multiples = generer_multiples(number, length)
print(f"Multiples de {number} : {multiples}")

# Daily Challenge - Challenge 2

def supprimer_consecutifs(chaine):
    if not chaine:
        return ""
    
    resultat = chaine[0]
    for lettre in chaine[1:]:
        if lettre != resultat[-1]:
            resultat += lettre
    
    return resultat

chaine = input("Entrez une chaîne de caractères : ")
nouvelle_chaine = supprimer_consecutifs(chaine)
print(f"Résultat : {nouvelle_chaine}")