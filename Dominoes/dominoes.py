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


while True:
    remainder, computer_pieces, player_pieces, start, player = distribution()
    print(f"""Stock pieces: {sorted(remainder)}
    Computer pieces: {sorted(computer_pieces)}
    Player pieces: {sorted(player_pieces)}
    Domino snake: {start}""")
    if player == 1:
        print("Status: player")
    elif player == 0:
        print("Status: computer")
    break
