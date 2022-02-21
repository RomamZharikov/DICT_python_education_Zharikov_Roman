import requests


class Parse:
    def __init__(self, currency):
        self.url = f"http://www.floatrates.com/daily/{currency}.json"
        self.response = requests.get(self.url).json()

    def request(self):
        try:
            return ['eur', self.response['eur']['rate']], ['usd', self.response['usd']['rate']]
        except KeyError:
            try:
                return ['eur', 1], ['usd', self.response['usd']['rate']]
            except KeyError:
                return ['eur', self.response['eur']['rate']], ['usd', 1]
