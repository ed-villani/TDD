from unittest import TestCase
from Money import Money

class TestDollar(TestCase):
    def setUp(self):
        pass
    def test_times(self):
        five = Money.Dollar(5)
        self.assertEqual(type(Money.Dollar(10)), type(five.times(2)))
        self.assertEqual(type(Money.Dollar(15)), type(five.times(3)))


    def test_equals(self):
        self.assertTrue(Money().dollar(5).equals(Money().dollar(5)))
        self.assertFalse(Money().dollar(5).equals(Money().dollar(6)))
        self.assertTrue(Money().franc(5).equals(Money().franc(5)))
        self.assertFalse(Money().franc(5).equals(Money().franc(6)))
        self.assertFalse(Money().dollar(5).equals(Money().franc(6)))


    def test_FrancMultiplication(self):
        five: Money = Money().franc(5)
        self.assertEqual(type(Money().franc(10)), type(five.times(2)))
        self.assertEqual(type(Money().franc(15)), type(five.times(3)))