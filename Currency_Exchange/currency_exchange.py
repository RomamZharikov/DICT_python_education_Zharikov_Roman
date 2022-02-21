from parse import Parse
from json import JSONDecodeError


class CurrencyExchange:
    def __init__(self, current_code):
        self.code = current_code
        self.my_coin = 0

    def conversion(self):
        while True:
            try:
                rate = Parse(self.code).request()
                break
            except JSONDecodeError:
                print("Please, enter a valid currency code")
                self.code = input("Please, enter currency code: ")
        for i in rate:
            print(f"The {self.code.upper()} to {i[0].upper()} exchange rate is {i[1]}")


def value_error(string):
    while True:
        try:
            i = float(input(string))
            return i
        except ValueError:
            print("Please enter a number")


if __name__ == "__main__":
    code = input("Please, enter currency code: ")
    a = CurrencyExchange(code)
    a.conversion()
