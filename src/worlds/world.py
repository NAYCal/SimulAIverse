from src.states.state import State


class World:
    def __init__(self, initial_state: State, size):
        self.walls = None
        self.size = size
        self.state = initial_state

    def perform_action(self):
        self = self.state.perform_action()

