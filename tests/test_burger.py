import pytest
from praktikum.burger import Burger
from conftest import create_bun,set_ingredients_one, set_ingredients_two


class TestBurger:
    def test_set_bun(self, create_bun):
        burger = Burger()
        burger.set_buns(create_bun)

        assert burger.bun == create_bun

    @pytest.mark.parametrize(
        'ingredient',
        [
            'set_ingredients_one',
            'set_ingredients_two'
        ]
    )
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, set_ingredients_one, set_ingredients_two):
        burger = Burger()
        burger.add_ingredient(set_ingredients_one)
        burger.add_ingredient(set_ingredients_two)
        burger.remove_ingredient(0)

        assert burger.ingredients == [set_ingredients_two]

    def test_move_ingredient(self, set_ingredients_one, set_ingredients_two):
        burger = Burger()
        burger.add_ingredient(set_ingredients_one)
        burger.add_ingredient(set_ingredients_two)
        burger.move_ingredient(1,0)

        assert set_ingredients_two == burger.ingredients[0]

    def test_get_price(self, create_bun, set_ingredients_one, set_ingredients_two):
        burger = Burger()
        burger.set_buns(create_bun)
        burger.add_ingredient(set_ingredients_one)
        burger.add_ingredient(set_ingredients_two)

        assert burger.get_price() == 6000.50

    def test_get_receipt(self, create_bun, set_ingredients_one, set_ingredients_two):
        burger = Burger()
        burger.set_buns(create_bun)
        ingredient_one = set_ingredients_one
        ingredient_two = set_ingredients_two
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        receipt = f'''(==== {burger.bun.get_name()} ====)
        = {str(ingredient_one.get_type()).lower()} {ingredient_one.get_name()} =
        = {str(ingredient_one.get_type()).lower()} {ingredient_two.get_name()} =
        (==== {burger.bun.get_name()} ====)'''


