friends = int(input("Enter the number of friends joining (including you):"))
if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[z - 1]: 0 for z in range(1, friends + 1)}
    print(new_dict)
    amount = int(input("Enter the total amount: "))
    if int(amount / friends) != (amount / friends):
        list_amount = [round((amount / friends), 2)] * friends
    else:
        list_amount = [round(amount / friends)] * friends
    new_dict_keys = list(new_dict.keys())
    new_dict_keys.sort()
    for i in range(len(new_dict_keys)):
        new_dict[new_dict_keys[i]] = list_amount[i]
    print(new_dict)
else:
    print("No one is joining for the party.")

friends = int(input("Enter the number of friends joining (including you):"))
if friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    name = [input() for i in range(friends)]
    new_dict = {name[z - 1]: 0 for z in range(1, friends + 1)}
    print(new_dict)
else:
    print("No one is joining for the party.")
