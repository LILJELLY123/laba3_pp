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
