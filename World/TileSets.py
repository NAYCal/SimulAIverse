from Graphic.AsciiRep import AsciiRep
from World.WorldTile import WorldTile


class TileSets:
    """
    Stores the tiles to be used.
    """

    EMPTY_SPACE = WorldTile(AsciiRep("  ", "black", "black"),
                            "This is an empty space.")
    FLOOR = WorldTile(AsciiRep("  ", "white", "white"),
                      "This is a floor. It stops you from falling.")
    WALL = WorldTile(AsciiRep("  ", "yellow", "yellow"),
                     "This is a wall. You do not want to run into it.")
