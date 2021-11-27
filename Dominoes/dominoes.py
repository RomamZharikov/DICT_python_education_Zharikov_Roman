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


def dominoes_check(dominoes, win):
    if dominoes[0][0] == dominoes[0][-1]:
        dominoes = list(chain(*dominoes))
        if dominoes.count(dominoes[0]) == 8:
            print("Status: The game is over. It's a draw!")
            win += 1
    return win


def game(computer_pieces, player_pieces, remainder, start, gamer_index):
    win = 0
    while win == 0:
        if win == 0:
            print("=" * 70)
            print(f"""Stock size: {len(remainder)}
Computer pieces: {len(computer_pieces)}\n""")
            if len(start) > 6:
                print(*start[:3], "...", *start[-3:])
            else:
                print(*start)
            print("\nYour pieces:")
            num = 1
            for i in player_pieces:
                print(f"{num}. {i}")
                num += 1
            if gamer_index == 0:
                while True:
                    try:
                        choice = int(input("Status: It's your turn to make a move. Enter your command:\n"))
                        break
                    except ValueError:
                        print("Illegal move. Please try again.")
                        pass
                win = dominoes_check(start, win)
                if 0 < choice <= len(player_pieces) != 0:
                    if player_pieces[choice - 1][0] == start[-1][1]:
                        start.append(player_pieces[choice - 1])
                        del player_pieces[player_pieces.index(player_pieces[choice - 1])]
                        gamer_index += 1
                    elif player_pieces[choice - 1][1] == start[-1][1]:
                        start.append(player_pieces[choice - 1][::-1])
                        del player_pieces[player_pieces.index(player_pieces[choice - 1])]
                        gamer_index += 1
                    else:
                        print("Illegal move. Please try again.")
                elif choice < 0 and abs(choice) <= len(player_pieces) != 0:
                    if player_pieces[abs(choice) - 1][1] == start[0][0]:
                        start.insert(0, player_pieces[abs(choice) - 1])
                        del player_pieces[player_pieces.index(player_pieces[abs(choice) - 1])]
                        gamer_index += 1
                    elif player_pieces[abs(choice) - 1][0] == start[0][0]:
                        start.insert(0, player_pieces[abs(choice) - 1][::-1])
                        del player_pieces[player_pieces.index(player_pieces[abs(choice) - 1])]
                        gamer_index += 1
                    else:
                        print("Illegal move. Please try again.")
                elif choice == 0 and len(remainder) != 0:
                    player_pieces.append(remainder[random.choice(range(len(remainder) - 1))])
                    del remainder[remainder.index(player_pieces[-1])]
                    gamer_index += 1
                elif abs(choice) > len(player_pieces):
                    print("Illegal move. Please try again.")
                elif len(computer_pieces) == 0 or choice == 0 and len(remainder) == 0:
                    print("Status: The computer win!")
                    break
                else:
                    win += 1
                    print("Status: You win!")
                    break
            elif gamer_index == 1 and len(player_pieces) != 0:
                print(len(input("Computer is about to make a move. Press Enter to continue...\n")) * "")
                win = dominoes_check(start, win)
                while True:
                    index = random.choice(range(-len(computer_pieces), len(computer_pieces) + 1))
                    if 0 < index <= len(computer_pieces) != 0:
                        if computer_pieces[index - 1][0] == start[-1][1]:
                            start.append(computer_pieces[index - 1])
                            del computer_pieces[computer_pieces.index(computer_pieces[index - 1])]
                            gamer_index -= 1
                            break
                        elif computer_pieces[index - 1][1] == start[-1][1]:
                            start.append(computer_pieces[index - 1][::-1])
                            del computer_pieces[computer_pieces.index(computer_pieces[index - 1])]
                            gamer_index -= 1
                            break
                    if index < 0 and abs(index) <= len(computer_pieces) != 0:
                        if computer_pieces[abs(index) - 1][1] == start[0][0]:
                            start.insert(0, computer_pieces[abs(index) - 1])
                            del computer_pieces[computer_pieces.index(computer_pieces[abs(index) - 1])]
                            gamer_index -= 1
                            break
                        elif computer_pieces[abs(index) - 1][0] == start[0][0]:
                            start.insert(0, computer_pieces[abs(index) - 1][::-1])
                            del computer_pieces[computer_pieces.index(computer_pieces[abs(index) - 1])]
                            gamer_index -= 1
                            break
                    if index == 0 and len(remainder) != 0:
                        computer_pieces.append(remainder[random.choice(range(len(remainder) - 1))])
                        del remainder[remainder.index(computer_pieces[-1])]
                        gamer_index -= 1
                        break
                    elif len(computer_pieces) == 0 or index == 1 and len(remainder) == 0:
                        print("Status: You win!")
                        break
            else:
                print("Status: You win!")
                break


a, b, c, d, e = distribution()
game(a, b, c, d, e)
