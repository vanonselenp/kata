import unittest


class TestConway(unittest.TestCase):
    def test_bad(self):
        add_bad(1)

        self.assertEqual(1, bad)

    def test_bad_1(self):
        add_bad(1)

        self.assertEqual(1, bad)

    def test_good(self):
        self.assertEqual(2, good_add(1, 1))

    def test_good_1(self):
        self.assertEqual(2, good_add(1, 1))


bad = 0

def add_bad(amount):
    global bad
    bad += amount

def good_add(existing, amount):
    return existing + amount

print(good_add(2,2))


def fn(a, b):
    return a * b


if __name__ == '__main__':
    bad = 0
    unittest.main()

 
