import random

from src.states.state import State


class World:
    def __init__(self, size):
        self.size = size
        self.walls = set()
        self.resources = set()
        self.states = {}

    def add_state(self, state):
        self.states[state.name] = state

    def get_state(self, state_name) -> State:
        return self.states[state_name]

    def get_initial_state(self) -> State:
        return self.states["initial"]

    def generate(self):
        # Create walls
        for i in range(self.size):
            self.walls.add((i, 0))
            self.walls.add((i, self.size - 1))
            self.walls.add((0, i))
            self.walls.add((self.size - 1, i))

        # Create resources
        num_resources = random.randint(1, 5)
        self.resources = set()
        for _ in range(num_resources):
            resource_pos = (random.randint(1, self.size - 2), random.randint(1, self.size - 2))
            self.resources.add(resource_pos)

    def is_empty(self) -> bool:
        return len(self.resources) == 0

    def reset(self):
        self.resources = set()

    def get_neighbor(self, position) -> []:
        x, y = position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if
                           0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.walls]

        return valid_neighbors
