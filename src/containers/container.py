class Container:
    """
    Helps facilitate transmission of data between classes through standardization of information.
    """

    def __init__(self, name, x_coord, y_coord, value):
        self.name = name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.value = value

    def open_container(self):
        return self.name, self.x_coord, self.y_coord, self.value
