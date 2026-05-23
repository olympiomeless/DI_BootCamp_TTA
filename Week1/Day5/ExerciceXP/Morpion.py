board = [""] * 9

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            index = move - 1
            if board[index] != "":
                print("Cell already taken, try again.")
                continue
            return index
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def place_marker(player, index):
    board[index] = player

def check_winner(mark):
    winning_combinations = [
        [6, 7, 8],   
        [3, 4, 5],   
        [0, 1, 2],   
        [0, 3, 6],   
        [1, 4, 7],   
        [2, 5, 8],   
        [0, 4, 8],   
        [2, 4, 6],   
    ]
    for combo in winning_combinations:
        if all(board[i] == mark for i in combo):
            return True
    return False

def check_draw():
    return "" not in board

def reset_board():
    global board
    board = [""] * 9

def play():
    players = {"Joueur 1": "X", "Joueur 2": "O"}
    while True:
        reset_board()
        current_player = "Joueur 1"

        for turn in range(9):
            mark = players[current_player]
            display_board()
            index = player_input(current_player)
            place_marker(mark, index)

            if check_winner(mark):
                display_board()
                print(f"{current_player} ({mark}) won!")
                break

            if check_draw():
                display_board()
                print("It's a draw!")
                break

            current_player = "Joueur 2" if current_player == "Joueur 1" else "Joueur 1"
        else:
            # loop completed without a break -> draw already handled, but ensure board shown
            display_board()
            print("It's a draw!")

        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")