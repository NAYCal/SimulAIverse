import random

from src.containers.container import Container


class ContainerFactory:
    """
    Helps set apart the types of containers between various types of simulation runs.
    """
    @staticmethod
    def open_container(container, size):
        if isinstance(container, Container):
            return container.open_container()
        else:
            name = container.name
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            value = container.value
            return name, x, y, value
