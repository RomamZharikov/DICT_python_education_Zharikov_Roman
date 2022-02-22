from parse import Parse, code_current
from json import JSONDecodeError


class CurrencyExchange:
    def __init__(self, current_code_in, coin, current_code_out):
        self.code_in = current_code_in
        self.code_out = current_code_out
        self.coin = coin
        self.used_coin = 0
        self.rate = Parse(self.code_in, self.code_out.lower())

    def conversion(self):
        while True:
            try:
                self.rate.currency_in = self.code_in
                self.rate.currency_out = self.code_out.lower()
                break
            except JSONDecodeError:
                print("Please, enter a valid currency code")
                self.code_in = input("Please, enter the currency to be transferred: ")
                self.code_out = input("What currency would you like to transfer to?: ")
        print(f"{self.coin * self.rate.request()} {self.code_out.upper()}")

    def balance(self):
        print("=" * 70)
        print(f"Balance: {self.coin}")

    def main(self):
        while True:
            if self.code_in == "".strip() or self.code_out == "".strip():
                break
            else:
                self.conversion()
                self.code_out = value_error("What currency would you like to transfer to?: ", 1)


def value_error(string, param):
    while True:
        if param == 1:
            i = input(string).lower()
            if i in code_current:
                return i
            else:
                print("Please, enter the correct currency")
        if param == 2:
            try:
                i = float(input(string))
                return i
            except ValueError:
                print("Please, enter a number")


if __name__ == "__main__":
    code_in = value_error("Please, enter the currency to be transferred: ", 1)
    code_out = value_error("What currency would you like to transfer to?: ", 1)
    my_coin = value_error("Please, enter the number of coins: ", 2)
    a = CurrencyExchange(code_in, my_coin, code_out)
    a.main()
