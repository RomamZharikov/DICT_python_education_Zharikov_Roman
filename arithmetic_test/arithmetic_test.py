from random import choice

num1 = choice(range(2, 9))
num2 = choice(range(2, 9))
result = int
action = choice(["*", "+", "-"])
print(f"{num1} {action} {num2}")
if action == "*":
    result = num1 * num2
elif action == "+":
    result = num1 + num2
elif action == "-":
    result = num1 - num2
while True:
    try:
        player_input = int(input())
        break
    except ValueError or TypeError:
        print("Incorrect format")
if result == player_input:
    print("Right!")
else:
    print("Wrong!")
