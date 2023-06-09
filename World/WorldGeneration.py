import random
from TileSets import TileSets


class WorldGeneration:
    def __init__(self, height=32, width=64, random_seed=None, tile_set=None):
        """
        Initialize a WorldGeneration instance.

        Parameters:
        - height (int, optional): The height of the generated world in tiles. Default is 32.
        - width (int, optional): The width of the generated world in tiles. Default is 64.
        - random_seed (int, optional): The random seed used for world generation. If not provided,
          a random seed between 0 and 9999 will be selected.
        - tile_set (list, optional): The tile set to be used for world generation. If not provided,
          a default tile set containing walls and floors will be used.
        """
        if random_seed is None:
            random_seed = random.randint(0, 9999)
        if tile_set is None:
            tile_set = [TileSets.WALL, TileSets.FLOOR]
        self.HEIGHT = height
        self.WIDTH = width
        self.random_seed = random_seed
        self.random = random.Random(random_seed)
        self.tile_set = tile_set
        self.tile_set.insert(0, TileSets.EMPTY_SPACE)

    def generate(self):
        """
        Generate a world with a predefined pattern.

        The first row and column of the generated world will be set as a border tile, and the remaining
        tiles will be randomly selected from the tile set.

        Returns:
        - generated_world (list of lists): The generated world represented as a 2D grid of tiles.
        """
        generated_world = [[self.tile_set[0]] * self.WIDTH for _ in range(self.HEIGHT)]
        for y in range(1, self.HEIGHT - 1):
            for x in range(1, self.WIDTH - 1):
                random_number = self.random.randint(1, len(self.tile_set) - 1)
                tile = self.tile_set[random_number]
                generated_world[y][x] = tile

        return generated_world


# Example usage
if __name__ == '__main__':
    generator = WorldGeneration()
    world = generator.generate()

    for row in world:
        for col in row:
            print(col, end='')
        print()
