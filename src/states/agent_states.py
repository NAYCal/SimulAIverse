from src.models.model import Model
from src.states.state import State
from src.worlds.world import World


class AgentState(State):
    """
    The base class for states regarding agents.
    """

    def __init__(self, name,  state_properties: {}, model: Model):
        super().__init__(name)
        self.state_resource = state_properties
        self.model = model

    def perform_action(self, world: World) -> {}:
        """
        Takes in the world object and performs the agent's action based on its current state. Instead of directly
        modifying the world object, it returns a map or object that represents the changes made by the agent's action.
        The map can contain information such as the agent's new position, any modifications to the environment, or any
        other relevant changes.
        :param world: The world where the agent resides in.
        :return: A map of actions by agent.
        """
        pass

    def perform_utility_action(self, world: World) -> {}:
        """
        Takes in the world object and performs any utility actions specific to the agent based on its current state.
        Similar to perform_action, it can return a map or object representing the changes made by the utility action.
        This allows the agent to perform auxiliary actions that may not directly modify the world but still have an
        impact on the simulation.
        :param world: The world where the agent resides in.
        :return: A map of actions by agent.
        """
        pass

    def transition_state(self) -> ():
        """
        This function allows the agent to evaluate its current state, consider any relevant properties, and decide
        which state to transition to based on the defined transition rules.
        :return: A tuple where the first object is the name of the next state based on data, and other properties to be
        passed.
        """
        return super().transition_state()


class SearchState(AgentState):
    """
    Represents the agent searching for a target or determining the next move based on pathfinding algorithms
    or exploration strategies.
    """


class ChaseState(AgentState):
    """
    Represents the agent actively pursuing a target once it has been identified or located.
    """


class ActState(AgentState):
    """
    Represents the agent performing an action or task once it reaches the target location.
    """


class RestState(AgentState):
    """
    Represents a state where the agent takes a break or remains inactive for a certain period, typically when there is
    no immediate motivation to act.
    """
