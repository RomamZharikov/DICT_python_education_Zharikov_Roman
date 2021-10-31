board = {11: "_", 12: "_", 13: "_",
         21: "_", 22: "_", 23: "_",
         31: "_", 32: "_", 33: "_"}
win = 1

def checkout():
    list_board = [value for value in board.values()]
    amount__ = list_board.count("_")
    global win
    if board[11] == board[22] == board[33] != "_":
        print(f"{board[11]} win!")
        win += 1
    elif board[13] == board[22] == board[31] != "_":
        print(f"{board[13]} win!")
        win += 1
    elif board[11] == board[12] == board[13] != "_":
        print(f"{board[11]} win!")
        win += 1
    elif board[21] == board[22] == board[23] != "_":
        print(f"{board[21]} win!")
        win += 1
    elif board[31] == board[32] == board[33] != "_":
        print(f"{board[31]} win!")
        win += 1
    elif board[11] == board[21] == board[31] != "_":
        print(f"{board[11]} win!")
        win += 1
    elif board[12] == board[22] == board[32] != "_":
        print(f"{board[12]} win!")
        win += 1
    elif board[13] == board[23] == board[33] != "_":
        print(f"{board[12]} win!")
        win += 1
    elif amount__ == 0:
        print("Draw")
        win -= 1
    else:
        print("")


def boards():
    print("-" * 7)
    print(f"""|{board[11]} {board[12]} {board[13]}|
|{board[21]} {board[22]} {board[23]}|
|{board[31]} {board[32]} {board[33]}|""")
    print("-" * 7)


def game_x():
    while win == 1:
        player = "X"
        answer = input(f"Please, input the coordinates (x y), player is {player}: ")
        coordinates = list(answer)
        if len(coordinates) == 2 :
            if 48 <= ord(coordinates[0]) <= 57 or 48 <= ord(coordinates[1]) <= 57:
                if int(coordinates[0]) <= 3 and int(coordinates[1]) <= 3:
                    numbers = int("".join(str(i) for i in coordinates))
                    if board[numbers] == "_":
                        board[numbers] = player
                        boards()
                        checkout()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                        boards()
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        elif len(coordinates) == 3:
            coordinates.remove(" ")
            if 48 <= ord(coordinates[0]) <= 57 or 48 <= ord(coordinates[1]) <= 57:
                if int(coordinates[0]) <= 3 and int(coordinates[1]) <= 3:
                    numbers = int("".join(str(i) for i in coordinates))
                    if board[numbers] == "_":
                        board[numbers] = player
                        boards()
                        checkout()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                        boards()
                else:
                    print("Coordinates should be from 1 to 3!")
        else:
            print("Please write down the coordinates in the format: '11' or '1 1'")



def game_o():
    while win == 1:
        player = "O"
        answer = input(f"Please, input the coordinates (x y), player is {player}: ")
        coordinates = list(answer)
        if len(coordinates) == 2:
            if 48 <= ord(coordinates[0]) <= 57 or 48 <= ord(coordinates[1]) <= 57:
                if int(coordinates[0]) <= 3 and int(coordinates[1]) <= 3:
                    numbers = int("".join(str(i) for i in coordinates))
                    if board[numbers] == "_":
                        board[numbers] = player
                        boards()
                        checkout()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                        boards()
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
        elif len(coordinates) == 3:
            coordinates.remove(" ")
            if 48 <= ord(coordinates[0]) <= 57 or 48 <= ord(coordinates[1]) <= 57:
                if int(coordinates[0]) <= 3 and int(coordinates[1]) <= 3:
                    numbers = int("".join(str(i) for i in coordinates))
                    if board[numbers] == "_":
                        board[numbers] = player
                        boards()
                        checkout()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                        boards()
                else:
                    print("Coordinates should be from 1 to 3!")
        else:
            print("Please write down the coordinates in the format: '11' or '1 1'")


boards()
while win == 1:
    game_x()
    game_o()


