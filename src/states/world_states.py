from src.states.state import State


class ResetState(State):
    """
    Represents a state where the world is reset, clearing any existing state or data, and preparing for a new round
    or iteration.
    """


class ActiveState(State):
    """
    Represents a state where the world is active and performing its normal operations.
    """


class GenerateState(State):
    """
    Represents a state where the world is generating or regenerating its environment, including terrain, resources,
    or other dynamic elements.
    """
