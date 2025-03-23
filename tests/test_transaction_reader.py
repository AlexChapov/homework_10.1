import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.transaction_reader import read_csv, read_excel


class TestExternalQuery(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="name,age\nVasya,30\nPetya,25")
    def test_read_csv(self, mock_file: MagicMock) -> None:
        """Тестируем функцию read_csv."""
        expected = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        result = read_csv("fake_path.csv")
        self.assertEqual(result, expected)

    @patch("csv.DictReader")
    @patch("builtins.open", new_callable=mock_open, read_data="fake data")
    def test_read_csv_dictreader(self, mock_file: MagicMock, mock_dictreader: MagicMock) -> None:
        """Тестируем функцию read_csv метод DictReader библиотеки csv."""
        mock_dictreader.return_value = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        expected_result = [{"name": "Vasya", "age": "30"}, {"name": "Petya", "age": "25"}]
        result = read_csv("fake_path.csv")
        self.assertEqual(result, expected_result)
