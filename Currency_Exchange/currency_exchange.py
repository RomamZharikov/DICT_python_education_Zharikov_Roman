class CurrencyExchange:
    def __init__(self, my_coin):
        self.my_coin = my_coin
        self.rate = [[0.82, "ARS"], [0.17, "HNL"], [1.9622, "AUD"], [0.208, "MAD"]]

    def conversion(self):
        for i in self.rate:
            print(f"I will get {round(i[0] * self.my_coin, 2)} {i[1]} from the sale of {self.my_coin} my_coins.")


def value_error(string):
    while True:
        try:
            i = float(input(string))
            return i
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    coin = value_error("Please, enter the number of my_coins you have: ")
    a = CurrencyExchange(coin)
    a.conversion()
