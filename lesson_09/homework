class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Currencies don't match")

    def __sub__(self, other):
        if self.currency == other.currency:
            if self.amount >= other.amount:
                return Price(self.amount - other.amount, self.currency)
            else:
                raise ValueError("Negative result")
        else:
            raise ValueError("Currencies don't match")

    def __str__(self):
        return f"{self.amount} {self.currency}"


price1 = Price(120, "USD")
price2 = Price(70, "USD")
price3 = Price(20, 'EUR')

# Addition with the same currency
result_addition = price1 + price2
print(f"Addition: {result_addition}")


# Subtraction with the same currency
result_subtraction = price1 - price2
print(f"Subtraction: {result_subtraction}")


# # Adding in different currencies
# result_addition = price1 + price3
# print(f"Addition: {result_addition}")