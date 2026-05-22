import random

class Game:
    ITEMS = ["rock", "paper", "scissors"]

    # Define the rules of the game: which item beats which
    WINS_AGAINST = {
        "rock"     : "scissors",   # rock crushes scissors
        "scissors" : "paper",      # scissors cut paper
        "paper"    : "rock"        # paper covers rock
    }
    
    #User choice her item
    def get_user_item(self):
        choice = input("Choose your item (rock, paper, scissors): ").strip().lower()
        if choice in self.ITEMS:
            return choice
        print(f"  Invalid choice. Please choose: {', '.join(self.ITEMS)}.")

    #Computer choice her item
    def get_computer_item(self):
        return random.choice(self.ITEMS)
    
    #Compare user item and computer item to determine the game results
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "Draw"
        elif self.WINS_AGAINST[user_item] == computer_item:
            return "Win"
        else:
            return "Loss"
    
    #Play the game
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        if user_item == computer_item:
            result = "Draw"
            message = "It's a draw!"

        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        ):
            result = "Win"
            message = "You won!"

        else:
            result = "Loss"
            message = "You lost!"

        # Affichage
        print(
            f"You chose {user_item}. "
            f"Computer chose {computer_item}. "
            f"{message}"
        )

        # Retour du résultat
        return result       