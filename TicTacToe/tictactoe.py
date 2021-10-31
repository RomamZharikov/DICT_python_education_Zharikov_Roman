list_board = list(input("Enter cells: "))
board_x = list_board.count("X")
board_o = list_board.count("O")
board__ = list_board.count("_")
winners = 0


def board():
    print("-" * 9)
    print(f"""|{list_board[0]} {list_board[1]} {list_board[2]}|
|{list_board[3]} {list_board[4]} {list_board[5]}|
|{list_board[6]} {list_board[7]} {list_board[8]}|""")
    print("-" * 9)


def rs_lt():
    global winners
    if list_board[0] == list_board[1] == list_board[2] != "_":
        print(list_board[0] + " wins")
        winners += 1
    elif list_board[3] == list_board[4] == list_board[5] != "_":
        print(list_board[3] + " wins")
        winners += 1
    elif list_board[6] == list_board[7] == list_board[8] != "_":
        print(list_board[6] + " wins")
        winners += 1
    elif list_board[2] == list_board[5] == list_board[8] != "_":
        print(list_board[2] + " wins")
        winners += 1
    elif list_board[0] == list_board[3] == list_board[6] != "_":
        print(list_board[0] + " wins")
        winners += 1
    elif list_board[0] == list_board[3] == list_board[6] != "_":
        print(list_board[0] + " wins")
        winners += 1
    elif list_board[1] == list_board[4] == list_board[7] != "_":
        print(list_board[1] + " wins")
        winners += 1
    elif list_board[2] == list_board[5] == list_board[8] != "_":
        print(list_board[2] + " wins")
        winners += 1
    elif board__ < 1:
        winners += 1
        print("Draw")


board()
player = "X"
while True:
    take = input("Enter the coordinates: ")
    coord = list(take)
    x, y = str(coord[2]), str(coord[0])
    if x.isalpha() or y.isalpha() or x == " " or y == " ":
        print("You should enter numbers!")
        continue
    elif y == "1":
        if x == "1":
            if str(list_board[0]) != "X" and list_board[0] != "O":
                list_board[0] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[1] != "X" and list_board[1] != "O":
                list_board[1] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[2] != "X" and list_board[2] != "O":
                list_board[2] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "2":
        if x == "1":
            if list_board[3] != "X" and list_board[3] != "O":
                list_board[3] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[4] != "X" and list_board[4] != "O":
                list_board[4] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[5] != "X" and list_board[5] != "O":
                list_board[5] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    elif y == "3":
        if x == "1":
            if list_board[6] != "X" and list_board[6] != "O":
                list_board[6] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "2":
            if list_board[7] != "X" and list_board[7] != "O":
                list_board[7] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        elif x == "3":
            if list_board[8] != "X" and list_board[8] != "O":
                list_board[8] = player
            else:
                print("This cell is occupied! Choose another one!")
                continue
        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("Coordinates should be from 1 to 3!")
        continue
    board()
    rs_lt()
    if winners > 0:
        break
    if player == "X":
        player = "O"
    else:
        player = "X"
