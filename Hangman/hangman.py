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
    for games in range(8):
        print("")
        letter = input("Input a letter:")
        for i in random_word:
            if letter == i:
                try_word.append(letter)
        if letter not in random_word:
            print("That letter doesn't appear in the word")
        print("")
        lines()
        if random_word_set == set(try_word):
            print('')
            print("You guessed the word!")
            print("You survived!")
            print('')
            break


print('HANGMAN')
print(len(random_word) * '-', end='')
game()
print("You lost!")
