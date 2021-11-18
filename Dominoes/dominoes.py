import random


def distribution():
    while True:
        domino_list = []
        for k in range(7):
            for j in range(7):
                if [j, k] in domino_list:
                    pass
                else:
                    domino_list.append([k, j])
        random.shuffle(domino_list)
        player_1 = domino_list[slice(0, 7)]
        player_2 = domino_list[slice(8, 15)]
        stock = [k for k in domino_list if k not in player_1 and k not in player_2]
        repeat1 = [player_1[k] for k in range(len(player_1)) if player_1[k] == player_1[k][::-1]]
        repeat2 = [player_2[k] for k in range(len(player_2)) if player_2[k] == player_2[k][::-1]]
        repeat = [repeat1, repeat2]
        first = []
        if len(repeat) > 1:
            for i in repeat:
                if i not in first:
                    first.append(i)
        elif len(repeat) == 1:
            first.append(repeat)
        if len(first) > 1:
            first.sort()
            first = first[-1]
        if len(first) == 1:
            if first[0] in player_1:
                for i, j in enumerate(player_1):
                    if j == first[0]:
                        del player_1[i]
                gamer = 0
                return player_1, player_2, stock, first, gamer
            elif first[0] in player_2:
                for i, j in enumerate(player_2):
                    if j == first[0]:
                        del player_2[i]
                gamer = 1
                return player_1, player_2, stock, first, gamer
            else:
                print("Error")


def game():
    computer_pieces, player_pieces, remainder, start, gamer_index = distribution()
    print("=" * 70)
    print(f"""Stock size: {len(remainder)}
Computer pieces: {len(computer_pieces)}\n""")
    print(*start)
    print("\nYour pieces:")
    num = 1
    for i in player_pieces:
        print(f"{num}. {i}")
        num += 1
    if gamer_index == 0:
        choice = int(input("Status: It's your turn to make a move. Enter your command:\n"))
        print(choice)
    elif gamer_index == 1:
        choice = int(input("Computer is about to make a move. Press Enter to continue...\n"))
        print(choice)


game()
