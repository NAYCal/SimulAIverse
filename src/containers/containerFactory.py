import random

from src.containers.container import Container


# TODO:Adjust for change of container format
class ContainerFactory:
    """
    Helps set apart the types of containers between various types of simulation runs.
    """

    @staticmethod
    def open_container(container, size):
        if isinstance(container, Container):
            return container.open_container()
        else:
            if len(container) != 2:
                raise TypeError("Container not Container class must be length 2!")
            if len(container[1] != 2):
                raise TypeError("Container value must contain at least representation and quantity!")
            name = container[0]
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            value = container[1]
            return name, x, y, value
