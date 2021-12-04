choice = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
if __name__ == "__main__":
    while True:
        input_player = input()
        if input_player in choice.keys():
            print(f"Sorry, but the computer chose {choice.get(input_player)}.")
            break
        else:
            print("Error")
