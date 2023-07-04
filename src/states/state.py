from abc import ABC, abstractmethod

from src.agents.agent import Agent
from src.worlds.world import World


class StateInterface(ABC):
    @abstractmethod
    def __getstate__(self):
        pass

    @abstractmethod
    def __setstate__(self, state):
        pass

    @abstractmethod
    def set_new_state(self, world: World, agent: Agent):
        pass

    @abstractmethod
    def get_valid_states(self) -> {}:
        pass

    @abstractmethod
    def is_end_state(self) -> ():
        pass


class State(StateInterface):

    def __getstate__(self):
        pass

    def __setstate__(self, state):
        pass

    def set_new_state(self, world: World, agent: Agent):
        pass

    def get_valid_states(self) -> {}:
        pass

    def is_end_state(self) -> ():
        pass
