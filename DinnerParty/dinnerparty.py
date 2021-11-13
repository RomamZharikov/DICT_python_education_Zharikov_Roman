import random

friends = int(input("Enter the number of friends joining (including you):"))
if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[z - 1]: 0 for z in range(1, friends + 1)}
    amount = int(input("Enter the total amount: "))
    if int(amount / friends) != (amount / friends):
        list_amount = [round((amount / friends), 2)] * friends
    else:
        list_amount = [round(amount / friends)] * friends
    new_dict_keys = list(new_dict.keys())
    new_dict_keys.sort()
    choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: ")
    if choice == "Yes":
        lucky_friend_index = random.choice(range(friends))
        for i in range(len(new_dict_keys)):
            new_dict[new_dict_keys[i]] = list_amount[i]
        print(f"{new_dict_keys[lucky_friend_index]} is the lucky one!")
    elif choice == "No":
        for i in range(len(new_dict_keys)):
            new_dict[new_dict_keys[i]] = list_amount[i]
        print("No one is going to be lucky.")
    print(new_dict)
else:
    print("No one is joining for the party.")
