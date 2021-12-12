print("""Hello! My name is Andrew.
I was created in 2021.
Please, remind me your name.""")                      #приветствие бота

name = input("")                                      #ввод имени пользователя
print(f"""What a great name you have, {name}! 
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.""")

rem3 = int(input(""))                                 #остаток от деления на 3 (введенное пользователем)
rem5 = int(input(""))                                 #остаток от деления на 5 (введенное пользователем)
rem7 = int(input(""))                                 #остаток от деления на 7 (введенное пользователем)
age = int(float((rem3 * 70 + rem5 * 21 + rem7 * 15) % 105)) #расчёт возраста

if age > 14:
    print(f"Your age is {age}; that's a good time to start programming!")
else:
    print(f"Your age is {age}; you so yong!")

print("Now I will prove to you that I can count to any number you want.")
number = int(float(input("")))                        #ввод числа до которого бот будет считать
num = float(-1)

for num in range(0, number+1, 1):                     #цикл от 0 с шагом в 1 цифру, number+1 - количество циклов
    print(f"{num}!")
print("Completed, have a nice day!")

print("""Let's test your programming knowledge.
Why do we use methods?""")
print("""1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.""")

questions = 4                                        #количество вопросов
answer = 2                                           #номер правильного ответа
result = int(input(""))                              #поле ввода правильного ответа
while result != answer:                              #запуск цикла
    if result == answer:                             #если ввели правильный ответ
        break                                        #конец цикла
    elif result > questions:                         #если ввели число большее чем количество вопросов
        print("There is no answer for this number.")
        result = int(input(""))
    else:                                            #если ввели неправильный ответ
        print("Please, try again.")
        result = int(input(""))

print("""Completed, have a nice day!
Congratulations, have a nice day!""")
