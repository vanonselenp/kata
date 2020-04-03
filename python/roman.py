import unittest


def toRoman(num):
    mapper = {
        10: 'X',
        5: 'V',
        1: 'I',
    }

    result = ""
    while num > 0:
        largest_key = 1
        for key, _ in mapper.items():
            if key <= num:
                largest_key = key
                break
        result += mapper[largest_key]
        num -= largest_key

    return result


class TestRoman(unittest.TestCase):
    def test_should_convert_1_to_I(self):
        self.assertEqual(toRoman(1), "I")

    def test_should_convert_2_to_II(self):
        self.assertEqual(toRoman(2), "II")
    
    def test_should_convert_3_to_III(self):
        self.assertEqual(toRoman(3), "III")

    def test_should_convert_5_to_V(self):
        self.assertEqual(toRoman(5), "V")

    def test_should_convert_6_to_VI(self):
        self.assertEqual(toRoman(6), "VI")

    def test_should_convert_10_to_X(self):
        self.assertEqual(toRoman(10), "X")

    def test_should_convert_10_to_X(self):
        self.assertEqual(toRoman(11), "XI")

if __name__ == '__main__':
    unittest.main()