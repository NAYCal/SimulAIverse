from src.states.state import State


class Agent:
    def __init__(self, agent_id: int):
        self.id = agent_id

    def set_initial_state(self):
        pass

    def perform_action(self):
        pass

    def perform_utility_action(self):
        pass

    def transition_state(self):
        pass
