import re
from datetime import datetime

def is_valid_email(email):
    # Prosty regex do sprawdzania e-maila
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Wymiary nie mogą być ujemne")
    return width * height

def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def convert_date_format(date_str):
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano dd-mm-yyyy.")

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]