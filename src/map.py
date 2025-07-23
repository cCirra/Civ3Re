class Map:
    """Represents a square grid map for the game."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # initialize grid with 'plains'
        self.tiles = [["plains" for _ in range(width)] for _ in range(height)]

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def set_tile(self, x, y, terrain):
        self.tiles[y][x] = terrain
