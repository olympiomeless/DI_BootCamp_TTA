from game import Game

def get_user_menu_choice():
    print("Welcome to Rock-Paper-Scissors Game!")
    choice = input("Enter the number of your choice: ").strip().lower()

    valid_choices = ["1", "2", "q", "exit"]
    if choice not in valid_choices:
        print(f"Invalid choice. Possible choices are : {', '.join(valid_choices)}")
        return None
    return choice

def print_results(results):
    total = sum(results.values())
    print(f"║  Victoires  : {results['Win']}║")
    print(f"║  Défaites   : {results['Loss']}║")
    print(f"║  Matchs nuls: {results['Draw']}║")
    print(f"║  Total      : {total}║")

def main():
    results = {
        "Win"  : 0,
        "Loss" : 0,
        "Draw" : 0
    }
    
    while True:
        choice = get_user_menu_choice()

        # If the choice is invalid, ask again
        if choice is None:
            continue

        # Play a game
        if choice == "1":
            game   = Game()
            result = game.play()        # retourne 'victoire', 'match nul' ou 'défaite'
            results[result] += 1        # mémoriser le résultat

        # Display results
        elif choice == "2":
            print_results(results)
            continue                    # ne pas quitter, rester dans la boucle

        # Exit the game
        elif choice in ("q", "x"):
            print_results(results)      # résumé final avant de quitter
            break                       # sortir de la boucle


# Point d'entrée
if __name__ == "__main__":
    main()