#One of the early common methods for encrypting text was the
#Playfair cipher. You can read more about the Playfair cipher
#here: https://en.wikipedia.org/wiki/Playfair_cipher
#
#The Playfair cipher starts with a 5x5 matrix of letters,
#such as this one:
#
# D A V I O
# Y N E R B
# C F G H K
# L M P Q S
# T U W X Z
#
#To fit the 26-letter alphabet into 25 letters, I and J are
#merged into one letter. When decrypting the message, it's
#relatively easy to tell from context whether a letter is
#meant to be an i or a j.
#
#To encrypt a message 
#-    1 ) first remove all non-letters

#-    2 ) convert the entire message to the same case.

#-    3 ) we break the message into pairs. 
# EG: imagine we wanted to encrypt the message 
# "PS. Hello, worlds". 
# First: we could convert it to PSHELLOWORLDS
# then: break it into letter pairs: 
# PS HE LL OW OR LD S. 
# If there is an odd number of characters: 
#    we add X to the end.
#
#-    4 ) for each pair of letters: 
#            we locate both letters in the cipher square. 
#
#There are four? possible orientations for the pair of letters: 
#    - the "rectangle" case: they could be in different rows and columns, 
#    - the "row" case: they could be in the same row but different columns (the "row" case),
#    - the "col" they could be in the same column but different rows (the "column"
#case), or they could be the same letter (the "same" case).
#
#Looking at the message PS HE LL OW OR LD SX:
#
# - PS is the Row case: P and S are in the same row.
# - HE is the Rectangle case: H and E are in different rows
#   and columns of the square.
# - LD is the Column case: L and D are in the same column.
# - LL is the Same case as it's two of the same letter.
#
#For the Same case, we replace the second letter in the pair
#with X, and then proceed as normal. When decrypting, it
#would be easy to see the our result was not intended to be
#PS HELXO WORLDSX, and we would thus assume the X is meant to
#repeat the previous letter, becoming PS HELLO WORLDSX.
#
#What we do for each of the other three cases is different:
#
# - For the Rectangle case, we replace each letter with
#   the letter in the same row, but the other letter's
#   column. For example, we would replace HE with GR:
#   G is in the same row as H but the same column as E,
#   and R is in the same row as E but the same column as
#   H. For another example, CS would become KL: K is in
#   C's row but S's column, and L is in C's column but S's
#   row.
# - For the Row case, we pick the letter to the right of
#   each letter, wrapping around the end of the row if we
#   need to. PS becomes QL: Q is to the right of P, and L
#   is to the right of S if we wrap around the end of the
#   row.
# - For the Column case, we pick the letter below each
#   letter, wrapping around if necessary. LD becomes TY:
#   T is below L and Y is below D.
#
#We would then return the resultant encrypted message.
#
#Decrypting a message is essentially the same process.
#You would use the exact same cipher and process, except
#for the Row and Column cases, you would shift left and up
#instead of right and down.
#
#Write two methods: encrypt and decrypt. encrypt should
#take as input a string, and return an encrypted version
#of it according to the rules above.
#
#To encrypt the string, you would:
#
# - Convert the string to uppercase.
# - Replace all Js with Is.
# - Remove all non-letter characters.
# - Add an X to the end if the length if odd.
# - Break the string into character pairs.
# - Replace the second letter of any same-character
#   pair with X (e.g. LL -> LX).
# - Encrypt it.
#
#decrypt should, in turn, take as input a string and
#return the unencrypted version, just undoing the last
#step. You don't need to worry about Js and Is, duplicate
#letters, or odd numbers of characters in decrypt.
#
#For example:
#
# encrypt("PS. Hello, world") -> "QLGRQTVZIBTYQZ"
# decrypt("QLGRQTVZIBTYQZ") -> "PSHELXOWORLDSX"

import unittest

CIPHER = (("D", "A", "V", "I", "O"),
          ("Y", "N", "E", "R", "B"),
          ("C", "F", "G", "H", "K"),
          ("L", "M", "P", "Q", "S"),
          ("T", "U", "W", "X", "Z"))


def format_characters(input):
    uppered = "".join([x.upper() for x in input if x.isalpha()])
    return uppered.replace("J", "I")


def pair_characters(input):
    if (len(input) % 2 != 0):
        input += "X"

    result = []

    for x in range(0, len(input), 2):
        a = input[x]
        second = input[x + 1]
        b = second if second != a else "X"
        result.append(a + b)

    return result


def prepare_data(input):
    formatted = format_characters(input)
    return pair_characters(formatted)


def is_row_case(input):
    for row in CIPHER:
        if input[0] in row and input[1] in row:
            return True
    return False


def apply_row_case(input, step=1):
    def get_character(s):
        return row[(row.index(s) + step) % 5]

    for r in CIPHER:
        if input[0] in r:
            row = r
            break

    a = get_character(input[0])
    b = get_character(input[1])
    return "%s%s" % (a, b)


def get_col(index):
    return  [
        CIPHER[0][index],
        CIPHER[1][index],
        CIPHER[2][index],
        CIPHER[3][index],
        CIPHER[4][index]
    ]


def is_col_case(input):
    for i in range(0, 5):
        col = get_col(i)
        if input[0] in col and input[1] in col:
            return True
    return False


def apply_col_case(input, step=1):
    for index in range(0, 5):
        col = get_col(index)
        if input[0] in col:
            break

    a = col[(col.index(input[0]) + step) % 5]
    b = col[(col.index(input[1]) + step) % 5]

    return "%s%s" % (a, b)


def apply_rectangle_case(input):
    for first_row in CIPHER:
        if input[0] in first_row:
            break

    for second_row in CIPHER:
        if input[1] in second_row:
            break

    a = first_row[second_row.index(input[1])]
    b = second_row[first_row.index(input[0])]

    return "%s%s" % (a, b)


def encrypt(input, step=1):
    data = prepare_data(input)

    result = []
    for pair in data:
        if is_row_case(pair):
            result.append(apply_row_case(pair, step))
        elif is_col_case(pair):
            result.append(apply_col_case(pair, step))
        else:
            result.append(apply_rectangle_case(pair))

    return "".join(result)


def decrypt(input):
    return encrypt(input, -1)


class TestFliarEncrypt(unittest.TestCase):
    def test_strip_non_alphabet_characters(self):
        self.assertEqual(format_characters("a"), "A")

    def test_replace_j_with_i(self):
        self.assertEqual(format_characters("j"), "I")

    def test_strip_white_space_from_characters(self):
        self.assertEqual(format_characters("a b"), "AB")

    def test_strip_numbers(self):
        self.assertEqual(format_characters("a 1"), "A")

    def test_return_in_pairs(self):
        self.assertEqual(pair_characters("ABCD"), ["AB", "CD"])

    def test_return_test_sentence_correctly(self):
        expected = ["PS", "HE", "LX", "OW", "OR", "LD", "SX"]
        self.assertEqual(prepare_data("PS. Hello, worlds"), expected)

    def test_is_row_case(self):
        self.assertEqual(is_row_case("PS"), True)

    def test_is_not_row_case(self):
        self.assertEqual(is_row_case("PH"), False)

    def test_apply_row_case(self):
        self.assertEqual(apply_row_case("PS"), "QL")

    def test_is_col_case(self):
        self.assertEqual(is_col_case("LD"), True)

    def test_is_not_col_case(self):
        self.assertEqual(is_col_case("DA"), False)

    def test_apply_col_case(self):
        self.assertEqual(apply_col_case("LD"), "TY")

    def test_rectangle_case(self):
        self.assertEqual(apply_rectangle_case("HE"), "GR")

    def test_rectangle_case_2(self):
        self.assertEqual(apply_rectangle_case("CS"), "KL")

    def test_encrypt(self):
        expected = "QLGRQTVZIBTYQZ"

        actual = encrypt("PS. Hello, worlds")

        self.assertEqual(actual, expected)

    def test_decrypt(self):
        expected = "PSHELXOWORLDSX"

        actual = decrypt("QLGRQTVZIBTYQZ")

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

