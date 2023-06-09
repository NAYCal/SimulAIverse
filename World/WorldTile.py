from Graphic.AsciiRep import AsciiRep


class WorldTile:
    """
    Represents a tile in the world.

    Attributes:
        ascii_rep (Str or AsciiRep): The ASCII representation of the tile.
        description (str): A description of the tile.
        entities (dict): A dictionary containing entities present on the tile.
    """

    def __init__(self, ascii_rep, description="", entities=None):
        """
        Initializes a new instance of the WorldTile class.

        Args:
            ascii_rep (Str or AsciiRep): The ASCII representation of the tile.
            description (str, optional): A description of the tile. Defaults to an empty string.
            entities (dict, optional): A dictionary containing entities present on the tile. Defaults to an empty dictionary.
        """
        if entities is None:
            entities = {}
        self.ascii_rep = ascii_rep
        self.description = description
        self.entities = entities

    def __str__(self):
        """
        Returns the string representation of the WorldTile.

        Returns:
            str: The ASCII representation of the tile.
        """
        return self.ascii_rep.__str__()


# Example usage
if __name__ == '__main__':
    tile8 = WorldTile(AsciiRep("8", "red"), "This is tile8")

    # Print the text representation
    print(tile8)
