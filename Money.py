class Money:
    def __init__(self):
        self.amount
    def equals(self, object):
        money = object
        return self.amount == money.amount


class Dollar:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier):
        self.amount = self.amount * multiplier


    def equals(self, object):
        dollar = object
        return self.amount == dollar.amount

class Franc:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier):
        self.amount = self.amount * multiplier


    def equals(self, object):
        franc = object
        return self.amount == franc.amount