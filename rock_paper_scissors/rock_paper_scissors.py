from random import choice

losing = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

if __name__ == "__main__":
    while True:
        input_player = input()
        if input_player in losing.keys():
            choice_pc = choice(list(losing.keys()))
            if choice_pc == losing.get(input_player):
                print(f"Sorry, but the computer chose {choice_pc}.")
            elif choice_pc == input_player:
                print(f"There is a draw ({choice_pc}).")
            elif losing.get(choice_pc) == input_player:
                print(f"Well done. The computer chose {choice_pc} and failed.")
        elif input_player == "!exit":
            print("Bye!")
            break
        else:
            print("Invalid input. Please, try again.")
