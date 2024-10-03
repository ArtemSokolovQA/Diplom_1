import pytest
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

    def test_remove_ingredient(self):
        burger = Burger()
        burger.add_ingredient(db.available_ingredients()[0])
        burger.remove_ingredient(0)
        assert not burger.ingredients

    def test_remove_ingredient_index_error(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self):
        burger = Burger()
        [burger.add_ingredient(i) for i in db.available_ingredients()[0:3]]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == db.available_ingredients()[1]

    def test_move_ingredients_moved_second_ingredient(self):
        burger = Burger()
        [burger.add_ingredient(i) for i in db.available_ingredients()[0:3]]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == db.available_ingredients()[0]

    def test_move_ingredients_index_error(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)

    def test_get_price(self):
        burger = Burger()
        burger.add_ingredient(db.available_ingredients()[0])
        burger.set_buns(db.available_buns()[0])
        assert burger.get_price() == 300

    def test_get_price_type_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt(self):
        burger = Burger()
        [burger.add_ingredient(i) for i in db.available_ingredients()]
        burger.set_buns(db.available_buns()[0])

        assert burger.get_receipt() == (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= sauce sour cream =\n'
            '= sauce chili sauce =\n'
            '= filling cutlet =\n'
            '= filling dinosaur =\n'
            '= filling sausage =\n'
            '(==== black bun ====)\n\n'
            'Price: 1400'
        )

    def test_get_price_attribute_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
