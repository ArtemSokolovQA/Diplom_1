from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun('Bulka', 0)
        assert bun.get_name() == 'Bulka'
        print(bun.get_name())

    def test_get_price(self):
        bun = Bun('dsdsjdsjdsjsdj', 0)
        assert bun.get_price() == 0

