import requests


class IEXStock:

    def __init__(self, token, symbol, environment='production'):
        if environment == 'production':
            self.base_url = 'https://cloud.iexapis.com/v1'
        else:
            self.base_url = 'https://sandbox.iexapis.com/v1'

        self.token = token
        self.symbol = symbol

    def get_logo(self):
        url = f'{self.base_url}/stock/{self.symbol}/logo?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_company_info(self):
        url = f'{self.base_url}/stock/{self.symbol}/company?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_company_news(self, last=10):
        url = f'{self.base_url}/stock/{self.symbol}/news/last/{last}?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_stats(self):
        url = f'{self.base_url}/stock/{self.symbol}/advanced-stats?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_fundamentals(self, period='quarterly', last=4):
        url = f'{self.base_url}/time-series/fundamentals/{self.symbol}/{period}?last={last}&token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_dividends(self, period='5y'):
        url = f'{self.base_url}/stock/{self.symbol}/dividends/{period}?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_institutional_ownership(self):
        url = f'{self.base_url}/stock/{self.symbol}/institutional-ownership?token={self.token}'
        r = requests.get(url)

        return r.json()

    def get_insider_transactions(self):
        url = f'{self.base_url}/stock/{self.symbol}/insider-transactions?token={self.token}'
        r = requests.get(url)

        return r.json()
