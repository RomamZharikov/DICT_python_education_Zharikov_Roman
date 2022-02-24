import requests


class Parse:
    def __init__(self, currency_in, currency_out):
        self.currency_in = currency_in
        self.url = f"http://www.floatrates.com/daily/{self.currency_in}.json"
        self.currency_out = currency_out
        self.check = 0
        self.response = requests.get(self.url).json()
        self.cache = {}
        if self.currency_in == "usd":
            self.cache = {"usd": 1, "eur": self.response["eur"]["rate"]}
        elif self.currency_in == "eur ":
            self.cache = {"eur": 1, "usd": self.response["usd"]["rate"]}
        else:
            self.cache = {"eur": self.response["eur"]["rate"], "usd": self.response["usd"]["rate"]}

    def request(self):
        print("Checking the cache...")
        if self.currency_in.lower() == self.currency_out:
            print("It is in the cache!")
            self.check = 0
            return 1
        elif self.currency_out in self.cache.keys():
            print("It is in the cache!")
            self.check = 0
            return self.cache[self.currency_out]
        else:
            print("Sorry, but it is not in the cache!")
            result = self.response[self.currency_out]["rate"]
            self.cache.update({self.currency_out.lower(): result})
            return result


code_current = ['eur', 'gbp', 'cad', 'jpy', 'aud', 'chf', 'lrd', 'sdg', 'top', 'vuv', 'hkd', 'thb', 'xaf', 'mdl', 'uyu',
                'mga', 'ttd', 'lak', 'bwp', 'jod', 'bgn', 'vnd', 'uzs', 'nio', 'cve', 'aoa', 'khr', 'nok', 'lkr', 'pln',
                'pen', 'iqd', 'stn', 'xpf', 'hnl', 'scr', 'dop', 'nzd', 'hrk', 'dzd', 'ars', 'bnd', 'kmf', 'lsl', 'tzs',
                'bbd', 'ang', 'pkr', 'krw', 'azn', 'crc', 'jmd', 'ssp', 'mru', 'mnt', 'brl', 'egp', 'sgd', 'zar', 'kgs',
                'pyg', 'srd', 'ghs', 'cup', 'dkk', 'inr', 'try', 'twd', 'tmt', 'afn', 'svc', 'sbd', 'zmw', 'yer', 'lbp',
                'huf', 'ngn', 'irr', 'mkd', 'bif', 'all', 'mur', 'ves', 'npr', 'isk', 'gip', 'gel', 'bzd', 'gnf', 'szl',
                'sos', 'aed', 'php', 'ils', 'mro', 'cop', 'gyd', 'rwf', 'ern', 'wst', 'cny', 'sar', 'myr', 'kzt', 'pab',
                'nad', 'syp', 'mop', 'bam', 'idr', 'tnd', 'xof', 'tjs', 'bob', 'etb', 'xcd', 'mwk', 'gtq', 'kwd', 'czk',
                'pgk', 'uah', 'gmd', 'awg', 'mmk', 'mvr', 'sek', 'mad', 'ron', 'byn', 'rsd', 'bsd', 'djf', 'sll', 'kes',
                'bhd', 'omr', 'rub', 'lyd', 'clp', 'fjd', 'cdf', 'mzn', 'ugx', 'bdt', 'qar', 'mxn', 'amd', 'htg',
                'usd', '']
