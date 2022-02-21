class CurrencyExchange:
    def __init__(self, my_coin, rate):
        self.my_coin = my_coin
        self.rate = rate

    def conversion(self):
        return self.my_coin * self.rate


def value_error(string):
    while True:
        try:
            i = float(input(string))
            return i
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    coin = value_error("Please, enter the number of my_coins you have: ")
    exchange_rate = value_error("Please, enter the exchange rate: ")
    a = CurrencyExchange(coin, exchange_rate)
    print(f"The total amount of dollars: {a.conversion()}")
