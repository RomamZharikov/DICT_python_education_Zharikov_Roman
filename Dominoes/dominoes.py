import random
from itertools import chain


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
            for j in repeat:
                if j not in first:
                    first.append(j)
        elif len(repeat) == 1:
            first.append(repeat)
        if len(first) > 1:
            first.sort()
            first = first[-1]
        if len(first) == 1:
            if first[0] in player_1:
                for k, j in enumerate(player_1):
                    if j == first[0]:
                        del player_1[k]
                gamer = 0
                return player_1, player_2, stock, first, gamer
            elif first[0] in player_2:
                for k, j in enumerate(player_2):
                    if j == first[0]:
                        del player_2[k]
                gamer = 1
                return player_1, player_2, stock, first, gamer
            else:
                print("Error")


def dominoes_check(winning, dominoes, pc, player):
    print(winning)
    if len(pc) == 0:
        print("Status: The computer win!")
        winning += 1
        return winning
    elif len(player) == 0:
        print("Status: You win!")
        winning += 1
        return winning
    elif dominoes[0][0] == dominoes[0][-1]:
        dominoes = list(chain(*dominoes))
        if dominoes.count(dominoes[0]) == 8:
            print("Status: The game is over. It's a draw!")
        else:
            return winning
    else:
        return winning


def logic_computer(dominoes):
    len_dominoes = len(dominoes)
    dominoes = list(chain(*dominoes))
    rare = {}
    for j in range(0, 7):
        rare[j] = dominoes.count(j)
    final_dict = {}
    len_dominoes_ = len(dominoes)
    for j in range(len_dominoes):
        dominoes.append(dominoes[j+j:2*j+2])
    del dominoes[:len_dominoes_]
    for j in dominoes:
        index_rare = rare.get(j[0])
        index_rare += rare.get(j[1])
        final_dict[dominoes.index(j)] = index_rare
    max_val = sorted(final_dict.items(), key=lambda x: x[1], reverse=True)
    final_list = [dominoes[j[0]] for j in max_val]
    return final_list


pc_pieces, player_pieces, rem, start, gm_index = distribution()
win = 0
while win == 0:
    win = dominoes_check(win, start, pc_pieces, player_pieces)
    print(win)
    if win == 0 and len(pc_pieces) != 0:
        print(f"""{"=" * 70}
Stock size: {len(rem)}
Computer pieces: {len(pc_pieces)}\n""")
        if len(start) > 6:
            print(*start[:3], "...", *start[-3:])
        else:
            print(*start)
        print("\nYour pieces:")
        num = 1
        for i in player_pieces:
            print(f"{num}. {i}")
            num += 1
        if gm_index == 0 and win == 0:
            while True:
                try:
                    choice = int(input("Status: It's your turn to make a move. Enter your command:\n"))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
            if 0 < choice <= len(player_pieces) != 0:
                if player_pieces[choice - 1][0] == start[-1][1]:
                    start.append(player_pieces[choice - 1])
                    del player_pieces[player_pieces.index(player_pieces[choice - 1])]
                    gm_index += 1
                elif player_pieces[choice - 1][1] == start[-1][1]:
                    start.append(player_pieces[choice - 1][::-1])
                    del player_pieces[player_pieces.index(player_pieces[choice - 1])]
                    gm_index += 1
                else:
                    print("Illegal move. Please try again.")
            elif choice < 0 and abs(choice) <= len(player_pieces) != 0:
                if player_pieces[abs(choice) - 1][1] == start[0][0]:
                    start.insert(0, player_pieces[abs(choice) - 1])
                    del player_pieces[player_pieces.index(player_pieces[abs(choice) - 1])]
                    gm_index += 1
                elif player_pieces[abs(choice) - 1][0] == start[0][0]:
                    start.insert(0, player_pieces[abs(choice) - 1][::-1])
                    del player_pieces[player_pieces.index(player_pieces[abs(choice) - 1])]
                    gm_index += 1
                else:
                    print("Illegal move. Please try again.")
            elif choice == 0 and len(rem) != 0:
                player_pieces.append(rem[random.choice(range(len(rem)))])
                del rem[rem.index(player_pieces[-1])]
                gm_index += 1
            elif choice == 0 and len(rem) == 0:
                print("Status: The computer win!")
                win += 1
                break
            else:
                win = dominoes_check(win, start, pc_pieces, player_pieces)
        elif gm_index == 1 and win == 0 and len(player_pieces) != 0:
            print(len(input("Computer is about to make a move. Press Enter to continue...\n")) * "")
            append = 0
            win = dominoes_check(win, start, pc_pieces, player_pieces)
            pc_pieces = logic_computer(pc_pieces)
            for i in range(len(pc_pieces) - 1):
                if pc_pieces[i][0] == start[-1][1] and append == 0:
                    start.append(pc_pieces[i])
                    del pc_pieces[pc_pieces.index(pc_pieces[i])]
                    gm_index -= 1
                    append += 1
                elif pc_pieces[i][1] == start[-1][1] and append == 0:
                    start.append(pc_pieces[i][::-1])
                    del pc_pieces[pc_pieces.index(pc_pieces[i])]
                    gm_index -= 1
                    append += 1
                elif pc_pieces[i][1] == start[0][0] and append == 0:
                    start.insert(0, pc_pieces[i])
                    del pc_pieces[pc_pieces.index(pc_pieces[i])]
                    gm_index -= 1
                    append += 1
                elif pc_pieces[i][0] == start[0][0] and append == 0:
                    start.insert(0, pc_pieces[i][::-1])
                    del pc_pieces[pc_pieces.index(pc_pieces[i])]
                    gm_index -= 1
                    append += 1
            if len(rem) != 0 and append == 0:
                pc_pieces.append(rem[random.choice(range(len(rem)))])
                gm_index -= 1
                append += 1
                del rem[rem.index(pc_pieces[-1])]
            elif append == 0:
                break
            else:
                win = dominoes_check(win, start, pc_pieces, player_pieces)
    else:
        break
