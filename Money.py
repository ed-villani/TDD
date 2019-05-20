class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def dollar(self, amount):
        return Dollar(amount, 'USD')

    def franc(self, amount):
        return Franc(amount, 'CHF')

    def currency(self):
        return self._currency

    def times(self, multipllier):
        pass

    def equals(self, object):
        money = object
        return self.amount == money.amount & (type(money) == type(Money))


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier) -> Money:
        return Money().dollar(self.amount * multiplier)

    def equals(self, object):
        dollar = object
        return self.amount == dollar.amount
    def currency(self):
        return self.currency

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier) -> Money:
        return Money().franc(self.amount * multiplier)

    def equals(self, object):
        franc = object
        return self.amount == franc.amount
    def currency(self):
        return self.currency
