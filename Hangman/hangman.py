import random
print("""Hello! Welcome to the game Hangman!
Try to guess the word.""")

index_word = random.randint(0, 3)
hidden_word = ["python", "java", "javascript", "php"]
selected_word = hidden_word[index_word]
word = str()

while word != selected_word:
    word = input("")
    if word == selected_word:
        print("You survived!")
    else:
        print("You lost!")
        break
