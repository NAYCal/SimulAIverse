from abc import ABC, abstractmethod

from src.states.state import State


class ModelInterface(ABC):
    @abstractmethod
    def next(self, start_state: State) -> {}:
        pass


class Model(ModelInterface):
    def next(self, start_state: State) -> {}:
        queue = []
        visited = {}
        end_state = None
        queue.append(start_state)

        while queue:
            state = queue.pop(0)

            if state.is_end_state():
                end_state = state
                break

            for child_state in state.get_valid_states():
                if child_state not in visited:
                    queue.append(child_state)
                    visited[child_state] = state

        path = []
        while end_state:
            path.insert(0, end_state)
            end_state = visited.get(end_state)

        return path
