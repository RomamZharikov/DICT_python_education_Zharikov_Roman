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
    list.clear(try_word)
    list.clear(try_wrong)
    hp = 8
    while hp > 0:
        print("")
        letter = input("Input a letter:")
        if letter in try_word:
            print("You've already guessed this letter.")
            print("")
            lines()
            continue
        if letter in try_wrong:
            print("You've already guessed this letter.")
            print("")
            lines()
            continue
        for i in random_word:
            if letter == i:
                try_word.append(letter)
        if letter.capitalize() == letter and len(letter) == 1:
            print("Please enter a lowercase English letter.")
            print("")
            lines()
            continue
        if len(letter) == 0 or len(letter) >= 2:
            print("You should input a single letter.")
            print("")
            lines()
            continue
        if letter not in random_word:
            try_wrong.append(letter)
            print("That letter doesn't appear in the word.")
            hp -= 1
            if hp == 0:
                print("You lost!")
                break
        print("")
        lines()
        if random_word_set == set(try_word):
            print('')
            print("You guessed the word " + random_word + "!")
            print("You survived!")
            print('')
            break


print("HANGMAN")
while True:
    print("Type 'play' to play the game, 'exit' to quit: ", end="")
    answer = input()
    if answer == "play":
        while True:
            print(len(random_word) * '-', end='')
            game()
            break
    elif answer == "exit":
        break
