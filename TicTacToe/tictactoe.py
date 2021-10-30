print(f"""{"-" * 9}
| _ _ _ |
| _ _ _ |
| _ _ _ |
{"-" * 9}""")


def checkout():
    amount_x = data.count("X")
    amount_o = data.count("O")
    amount__ = data.count("_")
    if amount_x == amount_o or amount_x == amount_o + 1 or amount_x == amount_o - 1:
        if amount__ == 0:
            if data[0] == data[3] == data[6] != "_":
                print(f"{data[0]} win!")
            elif data[1] == data[4] == data[7] != "_":
                print(f"{data[1]} win!")
            elif data[2] == data[5] == data[8] != "_":
                print(f"{data[2]} win!")
            elif data[0] == data[4] == data[8] != "_":
                print(f"{data[0]} win!")
            elif data[2] == data[4] == data[6] != "_":
                print(f"{data[2]} win!")
            elif data[0] == data[1] == data[2] != "_":
                print(f"{data[0]} win!")
            elif data[3] == data[4] == data[5] != "_":
                print(f"{data[3]} win!")
            elif data[6] == data[7] == data[8] != "_":
                print(f"{data[6]} win!")
            else:
                print("Draw")
        else:
            print("Game not finish")
    else:
        print("Impossible")


while True:
    entry = input("Please, enter a string consisting of 9 characters 'X', 'O' or '_': ")
    data = list(entry)
    if len(entry) == 9:
        print(f"""---------
| {data[0]} {data[1]} {data[2]} |
| {data[3]} {data[4]} {data[5]} |
| {data[6]} {data[7]} {data[8]} |
---------""")
        checkout()
        break
    else:
        print("try again")

