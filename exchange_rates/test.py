import argparse
from typing import Any
from pprint import pprint as print
import requests
import sys
from pydantic import BaseModel, Field

API_KEY = "HDKIKI6WAC2J677G"
BASE_URL = "https://www.alphavantage.co"


CACHE: dict[str, Any] = {}


# {'Realtime Currency Exchange Rate': {'1. From_Currency Code': 'USD',
#                                      '2. From_Currency Name': 'United States '
#                                                               'Dollar',
#                                      '3. To_Currency Code': 'JPY',
#                                      '4. To_Currency Name': 'Japanese Yen',
#                                      '5. Exchange Rate': '149.25300000',
#                                      '6. Last Refreshed': '2023-09-28 16:47:01',
#                                      '7. Time Zone': 'UTC',
#                                      '8. Bid Price': '149.24660000',
#                                      '9. Ask Price': '149.25710000'}}


def fetch_currency_exchange_rates(
    schema: AlphavantageCurrencyExchangeRatesRequest,
) -> AlphavantageCurrencyExchangeRatesResponse:
    """This function claims the currency exchange rate information
    from the external service: Alphavantage.
    """

    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return response


def initialize_args_parser():
    parser = argparse.ArgumentParser(
        prog="Currency exchange rates fatcher",
        description="This app claimes exchange rates from Alphavantage",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("--currency-from")
    parser.add_argument("--currency-to")

    return parser.parse_args()


def main():
    args: argparse.Namespace = initialize_args_parser()
    schema = AlphavantageCurrencyExchangeRatesRequest(
        currency_from=args.currency_from, currency_to=args.currency_to
    )
    result: AlphavantageCurrencyExchangeRatesResponse = (
        fetch_currency_exchange_rates(schema=schema)
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    main()