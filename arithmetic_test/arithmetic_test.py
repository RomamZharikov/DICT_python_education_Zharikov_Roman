from random import choice
from math import sqrt

try:
    with open("rating.txt", "r", encoding='utf-8') as rating:
        pass
except FileNotFoundError:
    with open("rating.txt", "w", encoding='utf-8') as rating:
        pass

annotation = str
used = []
result = int
sqrt_list = [i ** 2 for i in range(10, 33)]
leave = 0
allowed_values = ["yes", "y", "no", "n"]


if __name__ == "__main__":
    while True:
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
3 - found square root of 100-1024""")
        try:
            complexity = int(input().strip())
            if 0 < complexity <= 3:
                complexity = str(complexity)
                break
            else:
                print("There is no such level of difficulty. Try again!")
        except ValueError or TypeError:
            print("Incorrect format1")
    while leave == 0:
        grade = 0
        move = 1
        if complexity == "1":
            annotation = "simple operations with numbers 2-9"
        elif complexity == "2":
            annotation = "integral squares of 11-29"
        elif complexity == "3":
            annotation = "found square root of 100-1024"
        print(f"Your choice: {annotation}. Good luck!\n")
        while move < 6:
            if complexity == "1":
                num1 = choice(range(2, 10))
                num2 = choice(range(2, 10))
                action = choice(["*", "+", "-"])
                print(f"{num1} {action} {num2}")
                if action == "*":
                    result = num1 * num2
                elif action == "+":
                    result = num1 + num2
                elif action == "-":
                    result = num1 - num2
            elif complexity == "2":
                while True:
                    num1 = choice(range(11, 30))
                    if num1 not in used:
                        result = num1 ** 2
                        print(num1)
                        break
                used.append(num1)
            elif complexity == "3":
                while True:
                    num1 = choice(sqrt_list)
                    if num1 not in used:
                        result = sqrt(num1)
                        print(num1)
                        break
                used.append(num1)
            while True:
                try:
                    player_input = int(input())
                    break
                except ValueError or TypeError:
                    print("Incorrect format")
            if result == player_input:
                print("Right!")
                grade += 1
            else:
                print("Wrong!")
            move += 1
        print(f"Your mark is {grade}/5.")
        if grade >= 3 and (int(complexity) != 3):
            print(f"Do you want to try {int(complexity) + 1} level?\nEnter yes or no.")
            while True:
                level_record = input().lower().strip()
                if level_record in allowed_values:
                    break
                else:
                    print("Unknown answer")
            if level_record == "yes" or level_record == "y":
                complexity = int(complexity) + 1
                complexity = str(complexity)
        else:
            print(f"Do you want to try replay {int(complexity)} level?\nEnter yes or no.")
            while True:
                level_record = input().lower().strip()
                if level_record in allowed_values:
                    break
                else:
                    print("Unknown answer")
            if level_record == "yes" or level_record == "y":
                pass
        if level_record == "no" or level_record == "n":
            print("Would you like to save your result to the file? \nEnter yes or no.")
            result_record = input().lower().strip()
            if result_record == "yes" or result_record == "y":
                name = input("What is your name? \n")
                with open("rating.txt", "a", encoding='utf-8') as rating:
                    rating.write(f"{name}: {grade}/{move} in level {complexity} ({annotation})\n")
                print("The results are saved in 'results.txt'.")
                break
            elif result_record == "no" or result_record == "n":
                print("Bye!")
                break
