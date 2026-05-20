# Daily Challenge: Challenge 1
word = input("Enter a word: ")

caracteres = {}

for index, char in enumerate(word):
    char = str(char)
    if char in caracteres:
        caracteres[char].append(index)
    else:
        caracteres[char] = [index]

print(caracteres)

# Daily Challenge: Challenge 2
items_purchase = {
    "tam-tam": "100$",
    "shoes": "165$",
    "sneakers": "259$",
    "ball": "99$",
}

wallet = "1000$"

# Convert the wallet in int
def clean_price(price_str):
    for char in ['$', ',']:
        price_str = price_str.replace(char, '')
    return float(price_str)

# Convert the wallet
wallet_amount = clean_price(wallet)

# Create a manner
basket = []

for item, price in items_purchase.items():
    item_price = clean_price(price)
    if item_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= item_price

if not basket:
    print("Rien")
else:
    print(sorted(basket))