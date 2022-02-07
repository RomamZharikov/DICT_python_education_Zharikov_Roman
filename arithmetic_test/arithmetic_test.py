from random import choice


try:
    with open("rating.txt", "r", encoding='utf-8') as rating:
        pass
except FileNotFoundError:
    with open("rating.txt", "w", encoding='utf-8') as rating:
        pass

grade = 0
move = 1
annotation = str


def arithmetic_test(difficulty):
    result = int
    if difficulty == "1":
        num1 = choice(range(2, 9))
        num2 = choice(range(2, 9))
        action = choice(["*", "+", "-"])
        print(f"{num1} {action} {num2}")
        if action == "*":
            result = num1 * num2
        elif action == "+":
            result = num1 + num2
        elif action == "-":
            result = num1 - num2
    elif difficulty == "2":
        num1 = choice(range(11, 29))
        result = num1 ** 2
        print(num1)
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


if __name__ == "__main__":
    while True:
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
        try:
            complexity = int(input())
            if 0 < complexity <= 2:
                complexity = str(complexity)
                break
            else:
                print("There is no such level of difficulty. Try again!")
        except ValueError or TypeError:
            print("Incorrect format1")
    while move < 6:
        grade += arithmetic_test(complexity)
        move += 1
    print(f"Your mark is {grade}/5. \nWould you like to save your result to the file? \nEnter yes or no.")
    result_record = input().lower().strip()
    if result_record == "yes" or result_record == "y":
        name = input("What is your name? \n")
        if complexity == "1":
            annotation = "simple operations with numbers 2-9"
        elif complexity == "2":
            annotation = "integral squares of 11-29"
        with open("rating.txt", "a", encoding='utf-8') as rating:
            rating.write(f"{name}: {grade}/{move} in level {complexity} ({annotation})\n")
        print("The results are saved in 'results.txt'.")
    elif result_record == "no" or result_record == "n":
        print("Bye!")
