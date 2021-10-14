print("""Hello! Welcome to the game Hangman!
Try to guess the word.""")
hidden_word = str("python")
word = str()

while word != hidden_word:
    word = str(input("Guess the word:"))
    if word == hidden_word:
        print("You survived!")
    else:
        print("You lost!")
        break
