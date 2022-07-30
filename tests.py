import unittest
from MyNum.Numbers import Numbers


class  TestingNumbers(unittest.TestCase):

    def test__is_even(self):
        num = Numbers()
        num.number = 12
        self.assertTrue(num.is_even(), False)

    def test__is_odd(self):
        num = Numbers()
        num.number = 10000000001
        self.assertTrue(num.is_odd(), True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()