def coffeemachine():
    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    coffee = int(input("Write how many g of water the coffee machine has:\n"))
    amount = int(input("Write how many cups of coffee you will need:\n"))
    water_need = int(200 * amount)
    milk_need = int(50 * amount)
    coffee_need = int(15 * amount)
    max_cups = (min((water // 200), min((milk // 50), (coffee // 15))))
    print(f"""For {amount} cups of coffee you will need:
{water_need} ml of water
{milk_need} ml of milk
{coffee_need} g of coffee beans""")
    if max_cups > amount:
        print(f"Yes, I can make that amount of coffee (and even {max_cups - amount} more than that).")
    if max_cups == amount:
        print("Yes, I can make that amount of coffee.")
    if max_cups < amount:
        print(f"No, I can make only {max_cups} cups of coffee.")


coffeemachine()

