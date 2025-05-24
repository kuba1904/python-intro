import unittest
from app import (
    is_valid_email,
    calculate_rectangle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome
)

class TestAppFunctions(unittest.TestCase):

    # 1. Email
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_invalid_email_no_at(self):
        self.assertFalse(is_valid_email("testexample.com"))

    def test_invalid_email_empty(self):
        self.assertFalse(is_valid_email(""))

    # 2. Pole prostokąta
    def test_area_regular(self):
        self.assertEqual(calculate_rectangle_area(3, 4), 12)

    def test_area_zero(self):
        self.assertEqual(calculate_rectangle_area(0, 5), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-3, 5)

    # 3. Filtrowanie listy
    def test_filter_even(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_filter_empty(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_filter_all_odd(self):
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])

    # 4. Konwersja daty
    def test_date_conversion(self):
        self.assertEqual(convert_date_format("24-05-2025"), "2025/05/24")

    def test_date_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2025-05-24")

    def test_date_empty(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    # 5. Palindrom
    def test_palindrome_simple(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("A to idiota"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("python"))

if __name__ == "__main__":
    unittest.main()