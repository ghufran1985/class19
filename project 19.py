import random

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def dw(player, computer):
    if player == computer:
        return "It's a tie!"
    
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if win_conditions[player] == computer:
        return "You win! "
    else:
        return "You lose! "

def play():
    print("Welcome to Rock Paper Scissors")
    print("1: Rock ")
    print("2: Paper ")
    print("3: Scissors ")
    
    choices = {1: "rock", 2: "paper", 3: "scissors"}

    while True:
        try:
            player_input = input("Choose 1, 2, or 3 or type '4' to quit: ").strip()

            if player_input.lower() == "4":
                print("Thanks for playing! Goodbye!")
                break

            player_choice = int(player_input)

            if player_choice not in choices:
                print("Invalid choice! Please choose 1, 2, or 3.")
                continue

            player_move = choices[player_choice]
            computer_move = computer_choice()

            print(f"You chose: {player_move}")
            print(f"Computer chose: {computer_move}")

            result = dw(player_move, computer_move)
            print(result)
            print("-" * 30)

        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")

play()