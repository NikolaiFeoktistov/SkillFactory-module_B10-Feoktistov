import json
import requests

from config import keys


class ConversionException(Exception):
    pass


class СurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Неправильно введена валюта.Проверьте корректность ваших данных.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Неправильно введена валюта. Проверьте корректность ваших данных.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
