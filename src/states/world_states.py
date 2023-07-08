from src.states.state import State


class WorldState(State):
    """
    The base class for states regarding worlds.
    """

    def __init__(self, name):
        super().__init__(name)

    def perform_action(self):
        """
        Performs the primary action for the world state, such as generating the world or applying changes to the world.
        It returns the representation of the world. Additionally, it may record any interesting changes or store
        important information during this stage.
        :return: A representation of the world. E.g A grid or a 1D array.
        """
        super().perform_action()

    def perform_utility_action(self, properties: {}):
        """
        Takes in a map or object of properties and handles any conflict handling or additional actions on the world.
        It can modify the properties or make adjustments to the world based on the received properties. It returns an
        updated map or object representing the properties after handling.
        :param properties: A map of properties done onto the map, typically by agents.
        :return: A map of properties after handling the input properties.
        """
        super().perform_utility_action()

    def transition_state(self):
        """
        Checks the current properties of the world state and determines if there is a need to switch states. It returns
        the next state object based on the properties and the state transition rules. The transition_state method can
        also accept any necessary properties or information needed for the next state.
        :return: The next state based on stored properties.
        """
        super().transition_state()


class ResetState(WorldState):
    """
    Represents a state where the world is reset, clearing any existing state or data, and preparing for a new round
    or iteration.
    """


class ActiveState(WorldState):
    """
    Represents a state where the world is active and performing its normal operations.
    """


class GenerateState(WorldState):
    """
    Represents a state where the world is generating or regenerating its environment, including terrain, resources,
    or other dynamic elements.
    """
