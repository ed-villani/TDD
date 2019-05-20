from unittest import TestCase
from Money import Dollar

class TestDollar(TestCase):
    def setUp(self):
        pass
    def test_times(self):
        five = Dollar(5)
        five.times(2)
        self.assertEquals(10, five.amount)
