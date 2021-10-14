import random

hidden_word = ["python", "java", "javascript", "php"]
random_word = random.choice(hidden_word)
random_word_set = set(random_word)
try_wrong = []
try_word = []


def lines():
    for letter in random_word:
        if letter in try_word:
            print(letter, end="")
        else:
            print("-", end="")


def game():
    hp = 8
    while hp > 0:
        print("")
        letter = input("Input a letter:")
        if letter in try_word:
            print("No improvements")
            hp -= 1
            if hp == 0:
                print("You lost!")
                break
        for i in random_word:
            if letter == i:
                try_word.append(letter)
        if letter not in random_word:
            print("That letter doesn't appear in the word")
            hp -= 1
            if hp == 0:
                print("You lost!")
                break
        print("")
        lines()
        if random_word_set == set(try_word):
            print('')
            print("You guessed the word!")
            print("You survived!")
            print('')
            break


print('HANGMAN')
while True:
    print(len(random_word) * '-', end='')
    game()
    break
