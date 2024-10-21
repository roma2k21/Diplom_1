from praktikum.ingredient import Ingredient
from data import DataForTest

class TestIngredient:
    def test_get_price(self):
        ingredient = Ingredient(DataForTest.ingredient_type, DataForTest.ingredient_name, DataForTest.ingredient_price)

        assert ingredient.get_price() == DataForTest.ingredient_price

    def test_get_name(self):
        ingredient = Ingredient(DataForTest.ingredient_type, DataForTest.ingredient_name, DataForTest.ingredient_price)

        assert ingredient.get_name() == DataForTest.ingredient_name

    def test_get_type(self):
        ingredient = Ingredient(DataForTest.ingredient_type, DataForTest.ingredient_name, DataForTest.ingredient_price)

        assert ingredient.get_type() == DataForTest.ingredient_type
