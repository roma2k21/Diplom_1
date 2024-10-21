import pytest
from praktikum.bun import Bun
from data import DataForTest


class TestBun:
    def test_get_name(self):
        bun = Bun(DataForTest.bun_name, DataForTest.bun_price)

        assert bun.get_name() == 'Картонная булка 3000'

    def test_get_price(self):
        bun = Bun(DataForTest.bun_name, DataForTest.bun_price)

        assert bun.get_price() == 1500.00
