print(f"""---------
| _ _ _ |
| _ _ _ |
| _ _ _ |
---------""")


while True:
    entry = input("Please, enter a string consisting of 9 characters 'X', 'O' or '_': ")
    data = list(entry)
    if len(entry) == 9:
        print(f"""---------
| {data[0]} {data[1]} {data[2]} |
| {data[3]} {data[4]} {data[5]} |
| {data[6]} {data[7]} {data[8]} |
---------""")
        break
    else:
        print("try again")
