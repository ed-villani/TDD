class Dollar:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier):
        self.amount = self.amount * multiplier


    def equals(self, object):
        dollar = object
        return amount == dollar.amount

class Franc:
    def __init__(self, amount):
        self.amount = amount;

    def times(self, multiplier):
        self.amount = self.amount * multiplier


    def equals(self, object):
        franc = object
        return amount == franc.amount