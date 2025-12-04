import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# удаляет пробелы в начале
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" привет", "привет"),
    ("   привет, Мир!", "привет, Мир!"),
    ("          PYTEST", "PYTEST"),
    ("   258", "258")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("54654", "54654"),
    ("", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# поиск искомого символа в строке
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Скайпро", "а", True),
    ("5628", "2", True),
    ("Привет, мир!", "!", True),
    ("Восьмое число", "В", True),
    ("день недели", " ", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("54654", "7", False),
    ("", " ", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# удаляет подстроки из строки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Скайпро", "а", "Скйпро"),
    ("5628", "2", "568"),
    ("Восьмое число", " ", "Восьмоечисло"),
    ("день недели", "день", " недели")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("54654", "7", "54654"),
    ("Скайпро", "55", "Скайпро"),
    ("", "", "")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected