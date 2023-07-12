import random


class Container:
    """
    Helps facilitate transmission of data between classes through standardization of information.
    """

    def __init__(self, name, representation, value, x_coord=None, y_coord=None):
        if x_coord is None:
            x_coord = random.randint(0, 10)
        if y_coord is None:
            y_coord = random.randint(0, 10)

        self.name = name
        self.representation = representation
        self.value = value
        self.x_coord = x_coord
        self.y_coord = y_coord

    def open_container(self):
        return self.name, self.x_coord, self.y_coord, self.value
