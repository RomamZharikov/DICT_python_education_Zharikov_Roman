from parse import Parse, code_current


class CurrencyExchange:
    def __init__(self, current_code_in, coin):
        self.code_in = current_code_in
        self.code_out = ""
        self.coin = coin
        self.coin_remainder = coin
        self.used_coin = 0
        self.use = int
        self.rate = Parse(self.code_in, self.code_out.lower())
        self.command = ["!balance", "!transactions", "!exchange", "!leave"]
        self.conversions = []

    def conversion(self):
        self.rate.currency_in = self.code_in
        self.rate.currency_out = self.code_out.lower()
        self.conversions.append(f"{self.use} {self.code_in.upper()} --> " +
                                f"{self.use * self.rate.request()} {self.code_out.upper()}")
        self.coin_remainder -= self.use
        print(round(float(self.conversions[-1].split()[-2]), 2), self.conversions[-1].split()[-1].upper())

    def balance(self):
        print("=" * 70)
        print(f"""Balance: 
        * At the beginning it was: {self.coin} {self.code_in.upper()}
        * Remainder: {self.coin_remainder} {self.code_in.upper()}""")

    def menu(self):
        while True:
            choice = input("=" * 70 + "\nPlease enter the command: ").lower().strip()
            if choice == "!balance" or choice == "!b":
                self.balance()
            elif choice == "!help" or choice == "!h":
                for i in self.command:
                    print(f"* {i}")
            elif choice == "!transactions" or choice == "!t":
                for i in range(len(self.conversions)):
                    print(f"{i + 1}). {self.conversions[i]}")
            elif choice == "!exchange" or choice == "!e":
                self.exchange()
            elif choice == "!leave" or choice == "!l":
                break
            else:
                print("Please, imput correct command!")

    def exchange(self):
        print("=" * 70)
        self.code_out = value_error("What currency would you like to transfer to?: ", 1)
        while True:
            self.use = value_error("How much do you want to use?: ", 2)
            if self.use <= self.coin_remainder:
                break
            else:
                print(f"Insufficient funds. Left {self.coin_remainder} {self.code_in.upper()}")
        if self.code_in == "".strip() or self.code_out == "".strip():
            print("You have entered the menu!")
            return
        else:
            self.conversion()


def value_error(string, param):
    while True:
        if param == 1:
            i = input(string).lower()
            if i in code_current:
                return i
            else:
                print("Please, enter the correct currency!\n" + "=" * 70)
        if param == 2:
            try:
                i = float(input(string))
                return i
            except ValueError:
                print("Please, enter a number!\n" + "=" * 70)


if __name__ == "__main__":
    print("=" * 70 + "\nWelcome to currency converter!\n" + "=" * 70)
    code_in = value_error("Please, enter your main currency: ", 1)
    my_coin = value_error("Please, enter the number of coins: ", 2)
    a = CurrencyExchange(code_in, my_coin)
    a.menu()
