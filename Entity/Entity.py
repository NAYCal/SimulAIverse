class Entity:
    """
    Represents an entity in the world.

    Attributes:
        ascii_rep (str): The ASCII representation of the entity.
        description (str): A description of the entity.
        properties (dict): A dictionary mapping string keys to different types of values representing the entity's properties.
    """

    def __init__(self, ascii_rep, description="", properties=None, movable_tiles=None):
        """
        Initializes an instance of the Entity class.

        Args:
            ascii_rep (str): The ASCII representation of the entity.
            description (str, optional): A description of the entity. Defaults to an empty string.
            properties (dict, optional): A dictionary mapping string keys to different types of values representing the
            entity's properties. Defaults to an empty dictionary.
        """
        if properties is None:
            properties = {}
        if movable_tiles is None:
            movable_tiles = {}
        self.ascii_rep = ascii_rep
        self.description = description
        self.properties = properties
        self.movable_tiles = movable_tiles
        self.current_tile = None

    def add_to_world(self, tile):
        if not self.is_movable(tile):
            return False

        self.current_tile = tile
        self.interact_with_tile(tile)

    def interact_with_tile(self, tile):
        x = 1 + 1

    def is_movable(self, tile):
        """
        Checks if the entity can move to a specific tile.

        Args:
            tile (str): The tile to check.

        Returns:
            bool: True if the entity can move to the tile, False otherwise.
        """
        if tile in self.movable_tiles:
            return self.movable_tiles[tile]
        return False

    def display(self):
        """
        Displays the ASCII representation and description of the entity.

        Returns:
            None
        """
        print(self.ascii_rep)
        print(self.description)

    def __str__(self):
        """
        Returns a string representation of the entity.

        Returns:
            str: The ASCII representation of the entity.
        """
        return self.ascii_rep.__str__()
