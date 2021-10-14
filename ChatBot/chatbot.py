print("""Hello! My name is Andrew.
I was created in 2021.
Please, remind me your name.""")

name = input("")
print(f"""What a great name you have, {name}!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")

rem3 = int(input(""))
rem5 = int(input(""))
rem7 = int(input(""))
age = int((rem3 * 70 + rem5 * 21 + rem7 * 15) % 105)

if age > 14:
    print(f"Your age is {age}; that's a good time to start programming!")
else:
    print(f"Your age is {age}; you so yong!")

print("Now I will prove to you that I can count to any number you want.")
number = int(input(""))
num = float(-1)

for num in range(0, number+1, 1):
    print(f"{num}!")
print("Completed, have a nice day!")
