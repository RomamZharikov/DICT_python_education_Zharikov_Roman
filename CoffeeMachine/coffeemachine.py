class Stock:
    def __init__(self):
        self.money = 550
        self.cup = 9
        self.coffee = 120
        self.milk = 540
        self.water = 400

    def fill(self):
        self.water += int(input("Write how many ml of water the coffee machine has:\n"))
        self.milk += int(input("Write how many ml of milk the coffee machine has:\n"))
        self.coffee += int(input("Write how many g of coffee the coffee machine has:\n"))
        self.cup += int(input("Write how many g of cup the coffee machine has:\n"))

    def espresso(self):
        if self.water >= 250 and self.coffee >= 16 and self.cup >= 1:
            self.water -= 250
            self.coffee -= 16
            self.cup -= 1
            self.money += 4
        else:
            print("Not enough resources.\n")

    def latte(self):
        if self.water >= 350 and self.coffee >= 20 and self.cup >= 1 and self.milk >= 75:
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cup -= 1
            self.money += 7
        else:
            print("Not enough resources.\n")

    def cappuccino(self):
        if self.water >= 200 and self.coffee >= 12 and self.cup >= 1 and self.milk >= 100:
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cup -= 1
            self.money += 6
        else:
            print("Not enough resources.\n")

    def take(self):
        print(f"I gave you {self.money} UAH.\n")
        self.money = self.money - self.money


objects = Stock()
while True:
    print(f"""The coffee machine has:
{objects.water} of water
{objects.milk} of milk
{objects.coffee} of coffee beans
{objects.cup} of disposable cups
{objects.money} of money \n""")
    action = str(input("Write action (buy, fill, take):\n"))
    if action == "buy":
        choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n"))
        if choice == 1:
            objects.espresso()
        if choice == 2:
            objects.latte()
        if choice == 3:
            objects.cappuccino()
        if choice > 3:
            print("No such coffee exists\n")
    if action == "fill":
        objects.fill()
    if action == "take":
        objects.take()
