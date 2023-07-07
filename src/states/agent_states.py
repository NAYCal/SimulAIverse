from src.states.state import State


class SearchState(State):
    """
    Represents the agent searching for a target or determining the next move based on pathfinding algorithms
    or exploration strategies.
    """


class ChaseState(State):
    """
    Represents the agent actively pursuing a target once it has been identified or located.
    """


class ActState(State):
    """
    Represents the agent performing an action or task once it reaches the target location.
    """


class RestState(State):
    """
    Represents a state where the agent takes a break or remains inactive for a certain period, typically when there is
    no immediate motivation to act.
    """
