from src.agents.agent import Agent
from src.states.state import State
from src.worlds.world import World


class SquareWorld(World):
    def __init__(self, size):
        super().__init__(size)
        self.walls = set()
        self.resources = set()
        self.states = {}
        self.agents = {}

    def add_state(self, state):
        super().add_state(state)

    def get_state(self, state_name) -> State:
        return super().get_state(state_name)

    def add_agent(self, agent: Agent):
        super().add_agent(agent)

    def get_initial_state(self) -> State:
        return super().get_initial_state()

    def generate(self):
        # Create walls
        for i in range(self.size):
            self.walls.add((i, 0))
            self.walls.add((i, self.size - 1))
            self.walls.add((0, i))
            self.walls.add((self.size - 1, i))

        self.reset_resources()

    def is_empty(self) -> bool:
        return super().is_empty()

    def reset_resources(self):
        super().reset_resources()

    def get_neighbors(self, position) -> []:
        return super().get_neighbors(position)