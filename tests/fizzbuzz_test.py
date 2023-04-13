import unittest
from src.fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):

    def test_divisible_by_3_but_not_5(self):
        self.assertEqual("Fizz", fizzbuzz(3))

    def test_divisible_by_3_but_not_5__fail(self):
        self.assertEqual("error", fizzbuzz(15))

    def test_divisible_by_5_but_not_3(self):
        self.assertEqual("Buzz", fizzbuzz(5))

    def test_divisible_by_5_but_not_3__fail(self):
        self.assertEqual("error", fizzbuzz(15))
    
    # def test_divisible_by_5(self):
    #     self.assertEqual("Buzz", number.divisible_by_5)
    
    # def test_divisible_by_7(self, number):
    #     self.assertEqual("7", number.divisible_by_7)

    # def test_divisible_by_3_and_5(self, number):
    #     self.assertEqual("FizzBuzz", number.divisible_by_3_and_5)