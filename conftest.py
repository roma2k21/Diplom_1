import pytest
from unittest.mock import Mock

from data import DataForTest


@pytest.fixture()
def create_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = DataForTest.bun_name
    bun_mock.get_price.return_value = DataForTest.bun_price
    return bun_mock


@pytest.fixture()
def set_ingredients_one():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = DataForTest.ingredient_type_one
    ingredient_mock.get_name.return_value = DataForTest.ingredient_name_one
    ingredient_mock.get_price.return_value = DataForTest.ingredient_price_one
    return ingredient_mock


@pytest.fixture()
def set_ingredients_two():
    ingredient_mock = Mock()
    ingredient_mock.get_type.return_value = DataForTest.ingredient_type_two
    ingredient_mock.get_name.return_value = DataForTest.ingredient_name_two
    ingredient_mock.get_price.return_value = DataForTest.ingredient_price_two
    return ingredient_mock
