from random import choice

losing = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
with open("rating.txt", "r", encoding='utf-8') as rating:
    score_table = {i: j for line in rating for i, j in [line.split()]}
    rating.close()

if __name__ == "__main__":
    name = input("Enter your name:")
    print(f"Hello, {name}")
    if name in score_table.keys():
        score = int(score_table.get(name))
    else:
        score = 0
    while True:
        input_player = input()
        if input_player in losing.keys():
            choice_pc = choice(list(losing.keys()))
            if choice_pc == losing.get(input_player):
                print(f"Sorry, but the computer chose {choice_pc}.")
            elif choice_pc == input_player:
                print(f"There is a draw ({choice_pc}).")
                score += 50
            elif losing.get(choice_pc) == input_player:
                print(f"Well done. The computer chose {choice_pc} and failed.")
                score += 100
        elif input_player == "!exit":
            print("Bye!")
            break
        elif input_player == "!rating":
            print(f"Your rating: {score}")
        else:
            print("Invalid input. Please, try again.")
