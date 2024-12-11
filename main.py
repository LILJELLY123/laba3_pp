import re
import requests
import unittest

# Регулярное выражение для поиска двоичных чисел
binary_regex = r'\b[01]+\b'

def is_multiple_of_3(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value % 3 == 0

def find_binaries(input_data):
    matches = re.findall(binary_regex, input_data)
    return [match for match in matches if is_multiple_of_3(match)]

def get_data_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def find_binaries_in_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return find_binaries(data)

def main():
    input_data = input("Введите строку с двоичными числами: ")
    print("Двоичные числа, кратные 3:", find_binaries(input_data))

    url = input("Введите URL для поиска двоичных чисел (или оставьте пустым): ")
    if url:
        try:
            data_from_url = get_data_from_url(url)
            print("Двоичные числа, кратные 3 из URL:", find_binaries(data_from_url))
        except Exception as e:
            print(f"Ошибка при получении данных из URL: {e}")

    file_path = input("Введите путь к файлу для поиска двоичных чисел (или оставьте пустым): ")
    if file_path:
        try:
            print("Двоичные числа, кратные 3 из файла:", find_binaries_in_file(file_path))
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

class TestBinarySearch(unittest.TestCase):
    def test_is_multiple_of_3(self):
        self.assertTrue(is_multiple_of_3('11'))
        self.assertTrue(is_multiple_of_3('110'))
        self.assertFalse(is_multiple_of_3('10'))
        self.assertFalse(is_multiple_of_3('100'))

    def test_find_binaries(self):
        input_data = "101 110 111 1000 1001"
        expected = ['110', '1001']
        self.assertEqual(find_binaries(input_data), expected)

    def test_find_binaries_empty(self):
        input_data = ""
        expected = []
        self.assertEqual(find_binaries(input_data), expected)

if __name__ == "__main__":
    main()
    unittest.main()
