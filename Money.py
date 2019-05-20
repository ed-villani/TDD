class Money:
    def __init__(self):
        self.amount = None
    def dollar(self, amount):
        return Dollar(amount)
    def franc(self, amount):
        return Franc(amount)
    def times(self, multipllier):
        pass
    def equals(self, object):
        money = object
        return self.amount == money.amount & (type(money) == type(Money))

class Dollar:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier) -> Money:
        return Dollar(self.amount * multiplier)


    def equals(self, object):
        dollar = object
        return self.amount == dollar.amount

class Franc:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier) -> Money:
        return Franc(self.amount * multiplier)


    def equals(self, object):
        franc = object
        return self.amount == franc.amount