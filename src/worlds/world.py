import random

from src.agents.agent import Agent
from src.states.state import State


class World:
    def __init__(self, size):
        self.walls = None
        self.size = size
        self.agents = {}
        self.states = None

    def add_agent(self, agent: Agent):
        self.agents[agent.id] = agent

    def get_initial_state(self) -> State:
        return self.states["initial"]

    def generate(self):
        # Create walls
        for i in range(self.size):
            self.walls.add((i, 0))
            self.walls.add((i, self.size - 1))
            self.walls.add((0, i))
            self.walls.add((self.size - 1, i))

        self.reset_resources()

    def is_empty(self) -> bool:
        return len(self.resources) == 0

    def reset_resources(self):
        # Create resources
        num_resources = random.randint(1, 5)
        self.resources = set()
        for _ in range(num_resources):
            resource_pos = (random.randint(1, self.size - 2), random.randint(1, self.size - 2))
            self.resources.add(resource_pos)

    def get_neighbors(self, position) -> []:
        x, y = position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if
                           0 <= nx < self.size and 0 <= ny < self.size and (nx, ny) not in self.walls]

        return valid_neighbors
