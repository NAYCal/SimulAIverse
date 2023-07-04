import random
from abc import ABC, abstractmethod
from typing import Callable


class WorldInterface(ABC):
    @abstractmethod
    def generate(self):
        pass


class World(WorldInterface):
    """
    World generates a basic square world based on input size, tiles, seed, generate_fn.
    """

    def __init__(self, size: int, tiles=None, seed: int = 0, generate_fn: Callable = None):
        if tiles is None:
            tiles = [i for i in range(10)]

        if generate_fn is None:
            generate_fn = lambda i, j, world_size: random.choice(tiles)

        self.size = size
        self.seed = seed
        self.tiles = tiles
        self.generate_fn = generate_fn
        random.seed(self.seed)

    def generate(self):
        grid = [[None] * self.size] * self.size

        for i in range(self.size):
            for j in range(self.size):
                grid[i][j] = self.generate_fn(i, j, self.size)

        return grid

    def main(self):
        grid = self.generate()
        for i in range(self.size):
            for j in range(self.size):
                print(grid[i][j], end='  ')
            print()


if __name__ == "__main__":
    world = World(size=5)
    world.main()
