from src.game import Game
from src.unit import Unit
from src.city import City


def main():
    game = Game()
    settler = Unit('Settler', 0, 0)
    game.add_unit(settler)
    capital = City('Capital', 0, 0)
    game.add_city(capital)

    for turn in range(5):
        game.turn()
        print(f'Turn {turn+1}: {capital.name} population = {capital.population}')


if __name__ == '__main__':
    main()
