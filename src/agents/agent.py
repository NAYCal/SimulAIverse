from src.states.state_manager import StateManager


class Agent:
    def __init__(self, agent_id: int, agent_states: StateManager):
        self.id = agent_id
        self.states = agent_states

    def perform_action(self):
        pass

    def perform_utility_action(self):
        pass
