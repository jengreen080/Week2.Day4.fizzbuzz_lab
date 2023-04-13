import unittest
from src.fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):

    def test_divisible_by_3_but_not_5(self):
        self.assertEqual("Fizz", fizzbuzz(9))

    def test_divisible_by_5_but_not_3(self):
        self.assertEqual("Buzz", fizzbuzz(20))

    def test_divisable_by_neither(self):
        self.assertEqual("8", fizzbuzz(8))

    def test_divisible_by_5_and_3(self):
        self.assertEqual("FizzBuzz", fizzbuzz(30))
