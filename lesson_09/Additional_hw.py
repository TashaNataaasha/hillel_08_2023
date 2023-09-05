class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Currencies don't match")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        else:
            raise ValueError("Currencies don't match")

    def convert_to(self, target_currency: str, exchange_rate: float):
        if self.currency == target_currency:
            return self
        else:
            converted_amount = round(self.amount * exchange_rate, 2)
            return Price(converted_amount, target_currency)

price1 = Price(100, "USD")
price2 = Price(50, "USD")

total_price = price1 + price2
print(total_price.amount)  

difference = price1 - price2
print(difference.amount)  

price3 = Price(100, "USD")
price4 = Price(50, "EUR")

# Конвертируем price3 в EUR по курсу 0.85
converted_price = price3.convert_to("EUR", 0.85)
print(converted_price.amount)  
print(converted_price.currency)

# Конвертируем price4 в USD по курсу 1.18
converted_price = price4.convert_to("USD", 1.18)
print(converted_price.amount) 
print(converted_price.currency) 