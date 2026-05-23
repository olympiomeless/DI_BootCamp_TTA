from datetime import date

def is_leap_year(year):
    """Retourne True si l'année est bissextile."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year 
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

def display_cake(candles):

    if candles ==0:
        candles = 1
    
    candle_row = "" + "iiiii" * candles
    flame_row  = "      " + "|:H:a:p:p:y:|"
    
    print(candle_row)
    print(flame_row)
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

def main():
    print("🎂 Welcome to the Birthday Cake Generator!\n")

    birthdate = None  # ✅ initialiser AVANT la boucle

    while birthdate is None:  # ✅ boucler jusqu'à avoir une date valide
        try:
            birth_input  = input("Please enter your birthdate (DD/MM/YYYY): ").strip()
            day, month, year = map(int, birth_input.split("/"))

            current_year = date.today().year
            if year < 1900 or year > current_year:
                print(f"  ⚠️  Invalid year. Enter a year between 1900 and {current_year}.\n")
                continue  # ✅ birthdate reste None → la boucle continue

            temp_date = date(year, month, day)

            if temp_date > date.today():
                print("  ⚠️  Birthdate cannot be in the future.\n")
                continue  # ✅ birthdate reste None → la boucle continue

            birthdate = temp_date  # ✅ assigné seulement si tout est valide

        except ValueError:
            print("  ⚠️  Invalid format. Please use DD/MM/YYYY (e.g. 18/10/2000)\n")

    # ✅ On arrive ici seulement si birthdate est valide
    age     = calculate_age(birthdate)
    candles = age % 10

    print(f"\n🎉 You are {age} years old!")

    if is_leap_year(birthdate.year):
        print("🌟 You were born in a leap year! Here are two cakes!\n")
        display_cake(candles)
        print()
        display_cake(candles)
    else:
        print()
        display_cake(candles)

main()