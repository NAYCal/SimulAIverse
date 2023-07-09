from src.states.agent_states import AgentState
from src.states.state import State
from src.worlds.world import World


class StateManager:
    def __init__(self, states: {}, initial_state: State, *args):
        self.states = states
        self.current_state = initial_state

    def perform_action(self, *args) -> {}:
        return self.current_state.perform_action(args)

    def perform_utility_action(self, *args) -> {}:
        return self.current_state.perform_utility_action(args)

    def transition_state(self):
        state_container = self.current_state.transition_state()
        self.current_state = self.states[state_container[0]](state_container[1])


class AgentStateManager(StateManager):
    def __init__(self, states: {}, initial_state: AgentState, state_to_model: {}):
        super().__init__(states, initial_state)
        self.state_to_model = state_to_model

    def perform_action(self, world: World) -> {}:
        return super().perform_action(world)

    def perform_utility_action(self, world: World) -> {}:
        return super().perform_utility_action(world)

    def transition_state(self):
        state_container = self.current_state.transition_state()
        state = state_container[0]
        state_properties = state_container[1]
        state_model = self.state_to_model[state]

        self.current_state = self.states[state](state_properties, state_model)
