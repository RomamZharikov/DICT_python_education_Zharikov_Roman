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
        if self.water < 250:
            print("Sorry, not enough water!\n")
        elif self.coffee < 16:
            print("Sorry, not enough coffee!\n")
        elif self.cup < 1:
            print("Sorry, not enough cup!\n")
        else:
            self.water -= 250
            self.coffee -= 16
            self.cup -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!\n")

    def latte(self):
        if self.water < 350:
            print("Sorry, not enough water!\n")
        elif self.coffee < 20:
            print("Sorry, not enough coffee!\n")
        elif self.cup < 1:
            print("Sorry, not enough cup!\n")
        elif self.milk < 75:
            print("Sorry, not enough milk!\n")
        else:
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cup -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!\n")

    def cappuccino(self):
        if self.water < 200:
            print("Sorry, not enough water!\n")
        elif self.coffee < 12:
            print("Sorry, not enough coffee!\n")
        elif self.cup < 1:
            print("Sorry, not enough cup!\n")
        elif self.milk < 100:
            print("Sorry, not enough milk!\n")
        else:
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cup -= 1
            self.money += 6
            print("I have enough resources, making you a coffee!\n")

    def take(self):
        print(f"I gave you {self.money} UAH.\n")
        self.money = self.money - self.money

    def remaining(self):
        print(f"""The coffee machine has:
    -{self.water} of water;
    -{self.milk} of milk;
    -{self.coffee} of coffee beans;
    -{self.cup} of disposable cups;
    -{self.money} of money.\n""")


objects = Stock()
while True:
    action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
    if action == "buy":
        while action != "back":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu: \n")
            if choice == "1":
                objects.espresso()
                break
            if choice == "2":
                objects.latte()
                break
            if choice == "3":
                objects.cappuccino()
                break
    if action == "fill":
        objects.fill()
    if action == "take":
        objects.take()
    if action == "exit":
        break
    if action == "remaining":
        objects.remaining()
