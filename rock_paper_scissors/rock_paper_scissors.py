from random import choice
from math import floor, ceil

app, win, values = {}, {}, []
try:
    with open("rating.txt", "r", encoding='utf-8') as rating:
        score_table = {i: j for line in rating for i, j in [line.split()]}
except FileNotFoundError:
    with open("rating.txt", "w", encoding='utf-8') as rating:
        pass


def game_import():
    while True:
        link = input()
        if 0 == len(link) or len(link) >= 3:
            break
        else:
            print("Please, input >3 values or nothing for base values")
    if len(link) != 0:
        link = [str(i).strip().lower() for i in [*link.split(",")]]
        if len(link) % 2 == 1:
            for i in range(len(link)):
                for j in range(((len(link)) - 1) // 2):
                    values.append(link[i - j - 1])
                app.update({link[i]: values.copy()})
                values.clear()
            return app, None
        elif len(link) % 2 == 0:
            for i in range(len(link)):
                for j in range(floor(((len(link)) - 1) / 2)):
                    values.append(link[i - 1 - j])
                app.update({link[i]: values.copy()})
                values.clear()
            for i in app.keys():
                win.update({i: link[ceil(link.index(i) - 1 - (((len(link)) - 1) / 2))]})
            return app, win
    else:
        return {"rock": "paper", "paper": "scissors", "scissors": "rock"}, None


if __name__ == "__main__":
    name = input("Enter your name:")
    print(f"Hello, {name}")
    if name in score_table.keys():
        score = int(score_table.get(name))
    else:
        score = 0
    losing, win = game_import()
    print("Okay, let's start.")
    while True:
        input_player = input()
        if input_player in losing.keys():
            choice_pc = choice(list(losing.keys()))
            if choice_pc == input_player:
                print(f"There is a draw ({choice_pc}).")
                score += 50
            elif choice_pc in losing.get(input_player):
                print(f"Sorry, but the computer chose {choice_pc}.")
            elif input_player in losing.get(choice_pc):
                print(f"Well done. The computer chose {choice_pc} and failed.")
                score += 100
            else:
                if win.get(choice_pc) == input_player:
                    print(f"There is a draw ({choice_pc}).")
                    score += 50
        elif input_player == "!exit":
            print("Bye!")
            score_table.update({name: score})
            with open("rating.txt", "w+", encoding='utf-8') as rating:
                for i in score_table.keys():
                    rating.write(f"{i} {score_table.get(i)} \n")
            break
        elif input_player == "!rating":
            print(f"Your rating: {score}")
        else:
            print("Invalid input. Please, try again.")
