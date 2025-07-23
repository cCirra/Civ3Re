from .map import Map
from .unit import Unit
from .city import City

class Game:
    """Core game logic for the Civ3 remake."""

    def __init__(self, width=10, height=10):
        self.map = Map(width, height)
        self.units = []
        self.cities = []

    def add_unit(self, unit):
        self.units.append(unit)

    def add_city(self, city):
        self.cities.append(city)

    def turn(self):
        for city in self.cities:
            city.grow()
