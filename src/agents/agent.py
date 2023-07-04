from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def next(self):
        pass
