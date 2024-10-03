from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'cheese', 100)
        assert ingredient.get_price() == 100

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'cheese', 100)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'cheese', 100)
        assert ingredient.get_name() == 'cheese'


