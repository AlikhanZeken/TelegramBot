import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class ArtMoney:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количесвто {amount}')

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        exchange_rate = json.loads(r.content)[base_ticker]

        total_base = exchange_rate * amount

        return total_base

