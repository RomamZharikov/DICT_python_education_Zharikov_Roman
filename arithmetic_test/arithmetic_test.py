from random import choice


grade = 0
move = 0


def arithmetic_test():
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
        return 1
    else:
        print("Wrong!")
        return 0


while move < 5:
    grade += arithmetic_test()
    move += 1
print(f"Your mark is {grade}/5.")
