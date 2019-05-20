from unittest import TestCase
from Money import Dollar

class TestDollar(TestCase):
    def setUp(self):
        pass
    def test_times(self):
        five = Dollar(5)
        self.assertEquals(Dollar(10), five.times(2))
        self.assertEquals(Dollar(15), five.times(3))


    def test_equals(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertTrue(Dollar(5).equals(Dollar(6)))
