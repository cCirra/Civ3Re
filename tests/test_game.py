import unittest

from src.map import Map
from src.unit import Unit
from src.city import City
from src.game import Game

class TestGame(unittest.TestCase):
    def test_map_init(self):
        m = Map(5, 5)
        self.assertEqual(m.get_tile(0, 0), "plains")
        m.set_tile(1, 1, "grass")
        self.assertEqual(m.get_tile(1, 1), "grass")

    def test_unit_move(self):
        m = Map(3, 3)
        u = Unit("warrior", 0, 0)
        self.assertTrue(u.move(1, 1, m))
        self.assertEqual((u.x, u.y), (1, 1))
        self.assertFalse(u.move(3, 0, m))

    def test_city_growth(self):
        c = City("town", 0, 0)
        self.assertEqual(c.population, 1)
        c.grow()
        self.assertEqual(c.population, 2)

    def test_game_turn(self):
        g = Game(2, 2)
        c = City("town", 0, 0)
        g.add_city(c)
        g.turn()
        self.assertEqual(c.population, 2)

if __name__ == "__main__":
    unittest.main()
