from unittest import TestCase
from Money import Dollar
from Money import Franc

class TestDollar(TestCase):
    def setUp(self):
        pass
    def test_times(self):
        five = Dollar(5)
        self.assertEquals(Dollar(10), five.times(2))
        self.assertEquals(Dollar(15), five.times(3))


    def test_equals(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))
        self.assertTrue(Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))


    def test_FrancMultiplication(self):
        five = Franc(5)
        self.assertEquals(Franc(10), five.times(2))
        self.assertEquals(Franc(15), five.times(3))