from abc import ABC, abstractmethod


class Gui(ABC):
    @abstractmethod
    def display_state(self):
        pass

    @abstractmethod
    def get_input(self):
        pass
