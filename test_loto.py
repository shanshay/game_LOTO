import pytest
from class_loto import Gamer
from class_loto import Leading


class TestGamer:

    def test_create_card(self):
        gamer = Gamer('Nadya', 0, False)
        assert len(gamer.create_card()) == 27

    def test_init(self):
        gamer = Gamer('Nadya', 0, False)
        assert gamer.name == 'Nadya'
        assert gamer.count == 0
        assert gamer.test == False

    def test_check_count(self):
        gamer = Gamer(name='Nadya', count=15, test=False)
        gamer.check_count() == (f'Игра окончена! {gamer.name} выиграл! У {gamer.name} все цифры зачеркнуты!')

class TestLeading:

    def test_init(self):
        leading = Leading()
        leading.step = 15
        assert leading.step == 15
        assert len(leading.barrel) == 90
