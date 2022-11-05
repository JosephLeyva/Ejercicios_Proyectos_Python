class CurrenciesDoNotMatchError(Exception):
    def __init__(self, message, *args: object) -> None:
        super().__init__(message, *args)


class Currency:
    def __init__(self, currency, amount) -> None:
        self.currency = currency
        self.amount = amount

    def __repr__(self) -> str:
        return repr((self.currency, self.amount))

    def __add__(self, other):
        if self.currency != other.currency:
            raise CurrenciesDoNotMatchError(self.currency + " " + other.currency)
        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


value1 = Currency("USD", 20)
value2 = Currency("INR", 30)

print(value1 + value2)