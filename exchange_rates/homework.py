import argparse
import asyncio
import requests
from pydantic import BaseModel, Field

API_KEY = "HDKIKI6WAC2J677G"
BASE_URL = "https://www.alphavantage.co"

class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str

class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")

class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")

async def fetch_currency_exchange_rates(schema: AlphavantageCurrencyExchangeRatesRequest, target_currency: str):
    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return schema.currency_from, schema.currency_to, target_currency, response.results.rate

async def fetch_all_currency_exchange_rates(source_currencies, target_currency):
    tasks = []

    for source_currency in source_currencies:
        schema = AlphavantageCurrencyExchangeRatesRequest(currency_from=source_currency, currency_to=target_currency)
        task = asyncio.ensure_future(fetch_currency_exchange_rates(schema, target_currency))
        tasks.append(task)

    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"{result[0]} to {result[2]} rate: {result[3]}")

def initialize_args_parser():
    parser = argparse.ArgumentParser(
        prog="Currency exchange rates fetcher",
        description="This app fetches exchange rates from Alphavantage",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("source_currencies", nargs='+', help="Source currencies")
    parser.add_argument("--target", required=True, help="Target currency")
    return parser.parse_args()

def main():
    args = initialize_args_parser()
    source_currencies = args.source_currencies
    target_currency = args.target

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all_currency_exchange_rates(source_currencies, target_currency))

if __name__ == "__main__":
    main()