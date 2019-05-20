class Money:
    def __init__(self, amount, currency):
        if amount != '' and currency != '':
            self.amount = amount
            self._currency = currency
        else:
            self.amount = None
            self._currency = None

    def dollar(self, amount):
        return Money(amount, 'USD')

    def franc(self, amount):
        return Money(amount, 'CHF')

    def currency(self):
        return self._currency

    def times(self, multipllier):
        return Money(self.amount * multipllier, self.currency())

    def equals(self, object):
        money = object
        a = self.currency() == money.currency()
        b = self.amount == money.amount
        return a & b
