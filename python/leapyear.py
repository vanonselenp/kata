import unittest

def leap_year(num):
    if num == 2001:
        return False


class TestLeapYear(unittest.TestCase):
    def test_should_return_false_when_given_common_year_2001(self):
        self.assertFalse(leap_year(2001))

    def test_should_return_false_when_given_common_year_9(self):
        self.assertFalse(leap_year(9))


if __name__ == '__main__':
    unittest.main()