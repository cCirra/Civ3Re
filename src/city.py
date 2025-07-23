class City:
    """Represents a city with population."""

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.population = 1

    def grow(self):
        self.population += 1
