import unittest

def fizz_buzz(value: int) -> str:
    if value == 0:
        raise ValueError("Input can't be zero")

    result = ""

    if value % 3 == 0:
        result += 'Fizz'

    if value % 5 == 0:
        result += 'Buzz'

    return result if len(result) > 0 else "%s" % value 


class TestFizzBuzz(unittest.TestCase):
    def test_should_return_fizz_when_given_three(self):
        self.assertEquals(fizz_buzz(3), "Fizz")

    def test_should_return_fizz_when_given_nine(self):
        self.assertEquals(fizz_buzz(9), 'Fizz')

    def test_should_not_return_fizz_when_given_one(self):
        self.assertEquals(fizz_buzz(1), "1")
    
    def test_should_not_return_fizz_when_given_two(self):
        self.assertEquals(fizz_buzz(2), "2")

    def test_should_not_return_fizz_when_given_four(self):
        self.assertEquals(fizz_buzz(4), "4")

    def test_should_return_buzz_when_given_five(self):
        self.assertEquals(fizz_buzz(5), "Buzz")

    def test_should_return_buzz_when_given_ten(self):
        self.assertEquals(fizz_buzz(10), "Buzz")

    def test_should_return_buzz_when_given_20(self):
        self.assertEquals(fizz_buzz(20), "Buzz")

    def test_should_return_fizz_buzz_when_given_fifteen(self):
        self.assertEquals(fizz_buzz(15), "FizzBuzz")

    def test_should_return_fizz_buzz_when_given_thirty(self):
        self.assertEquals(fizz_buzz(30), "FizzBuzz")

    def test_should_return_fizz_buzz_when_given_forty_five(self):
        self.assertEquals(fizz_buzz(45), "FizzBuzz")
        
    def test_should_value_error_when_given_zero(self):
        with self.assertRaises(ValueError):
            fizz_buzz(0)


if __name__ == '__main__':
    unittest.main()