from unittest.mock import MagicMock, mock_open, patch

from src.utils import reading_json_file


@patch("json.loads")
def test_reading_json_file(mock_get):
    """Тест на проверку открытия пустого списка"""
    mock_get.return_value = []
    assert reading_json_file("../data/operations.json") == []


@patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
def test_correct_reading_json_file(mock_file: MagicMock):
    """Тест на проверку открытия файла с данными"""
    expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
    result = reading_json_file("fake.json")
    assert expected_data == result
    mock_file.assert_called_once_with("fake.json", "r", encoding="utf-8")
