water = 400
milk = 200
coffee = 100


def coffeemachine():
    amount = int(input("Write how many cups of coffee you will need: "))
    print(f"""For {amount} cups of coffee you will need:
{200 * amount} ml of water
{50 * amount} ml of milk
{15 * amount} g of coffee beans""")


coffeemachine()
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
