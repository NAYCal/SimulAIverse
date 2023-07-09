from src.states.state_manager import StateManager


class World:
    def __init__(self, size, world_states: StateManager):
        self.size = size
        self.states = world_states
        self.resources = {}

    def perform_action(self):
        pass

    def perform_utility_action(self, properties: {}):
        pass

    def add_resource(self, resource_name, resource_value):
        self.resources[resource_name] = resource_value

    def get_resource(self, resource_name):
        return self.resources[resource_name]
