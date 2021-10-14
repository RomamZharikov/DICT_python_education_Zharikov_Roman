import random
print("""Hello! Welcome to the game Hangman!
Try to guess the word.""")

index_word = random.randint(0, 3)
hidden_word = ["python", "java", "javascript", "php"]
selected_word = hidden_word[index_word]
word = str()

letters = list(selected_word)
hidden = letters[3:]
prompt = letters[:3]
number = len(hidden)
hidden_letters = []
car = ["-"]

for x in range(number):
    hidden_letters = hidden_letters + car

hint = prompt + hidden_letters
ready_hint = "".join(hint)

while word != selected_word:
    word = input(ready_hint + ": ")
    if word == selected_word:
        print("You survived!")
    else:
        print("You lost!")
        break
