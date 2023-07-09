from src.states.state import State


class WorldState(State):
    """
    The base class for states regarding worlds.
    """

    def __init__(self, name, state_resources: {}, *args):
        super().__init__(name)
        self.state_properties = state_resources

    def perform_action(self, *args):
        """
        Performs the primary action for the world state, such as generating the world or applying changes to the world.
        It returns the representation of the world. Additionally, it may record any interesting changes or store
        important information during this stage.
        :return: A representation of the world. E.g A grid or a 1D array.
        """
        return super().perform_action()

    def perform_utility_action(self, properties: {}, *args) -> {}:
        """
        Takes in a map or object of properties and handles any conflict handling or additional actions on the world.
        It can modify the properties or make adjustments to the world based on the received properties. It returns an
        updated map or object representing the properties after handling.
        :param properties: A map of properties done onto the map, typically by agents.
        :return: A map of properties after handling the input properties.
        """
        return super().perform_utility_action()

    def transition_state(self) -> ():
        """
        Checks the current properties of the world state and determines if there is a need to switch states. It returns
        the next state object based on the properties and the state transition rules. The transition_state method can
        also accept any necessary properties or information needed for the next state.
        :return: A tuple where the first object is the name of the next state based on data, and other properties to be
        passed.
        """
        return super().transition_state()


def default_generate_fn(x, y, size):
    if x == 0 or x == size - 1:
        return 0
    if y == 0 or y == size - 1:
        return 0
    return 1


class GenerateState(WorldState):
    """
    Represents a state where the world is generating or regenerating its environment, including terrain, resources,
    or other dynamic elements.
    """

    def __init__(self, name, state_resources: {}, size=10, generate_fn=None):
        if generate_fn is None:
            generate_fn = default_generate_fn
        super().__init__(name, state_resources)
        self.size = size
        self.generate_fn = generate_fn

    def perform_action(self):
        return [[self.generate_fn(x, y, self.size) for y in range(self.size)] for x in range(self.size)]

    def perform_utility_action(self, properties: {}, *args) -> {}:
        return super().perform_utility_action(properties, *args)

    def transition_state(self) -> ():
        return ActiveState, self.state_properties


class ResetState(WorldState):
    """
    Represents a state where the world is reset, clearing any existing state or data, and preparing for a new round
    or iteration.
    """


class ActiveState(WorldState):
    """
    Represents a state where the world is active and performing its normal operations.
    """
