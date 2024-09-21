import pytest
from praktikum import database
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database

db = Database()


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Bulka', 199)
        burger.set_buns(bun)
        assert burger.bun.name == 'Bulka'  # поскольку атрибуты не приватные, не использую метод get_name

    @pytest.mark.parametrize('ingredient', db.available_ingredients())
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

