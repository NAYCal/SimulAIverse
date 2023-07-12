from src.containers.containerFactory import ContainerFactory
from src.states.state import State


class WorldState(State):
    """
    The base class for states regarding worlds.
    """

    def __init__(self, name, state_resources: {}, *args):
        super().__init__(name)
        self.state_resources = state_resources

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

    def get_resources(self):
        return self.state_resources


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

# TODO: Adjust for change of container format
    def perform_utility_action(self, new_state_resources: dict, grid=None, is_replace=None, resource_placement_fn=None):
        """
        Adds resources onto the map destructively.

        :param new_state_resources: The new values of resources in the world. This assumes that the input resources are
        stored in the Container class, otherwise, random coordinates are generated for the resources
        :param grid: Optional. The format that stores the world grid. If not provided, it is generated using
        'perform_action()'.
        :param is_replace: Optional. A function that determines if resources in a tile can be replaced. Default is
        'lambda x, y, size, world_grid, new_value: True'.
        :param resource_placement_fn: Optional. A function that replaces the current tile. Default is 'lambda x, y,
        size, world_grid, new_value: new_value'.
        :return: A map of properties after handling the input properties.
        """
        # Set default values for optional parameters if not provided
        if grid is None:
            grid = self.perform_action()
        if is_replace is None:
            is_replace = lambda x_coord, y_coord, size, world_grid, new_value: True
        if resource_placement_fn is None:
            resource_placement_fn = lambda x_coord, y_coord, size, world_grid, new_value: new_value

        max_attempts = self.size * self.size // len(new_state_resources)

        for resource in new_state_resources.items():
            name, x, y, value = ContainerFactory.open_container(resource, self.size)
            attempts = 0

            while not is_replace(x, y, self.size, grid, value) and attempts < max_attempts:
                name, x, y, value = ContainerFactory.open_container(resource, self.size)
                attempts += 1

            if attempts >= max_attempts:
                raise Exception("Unable to find a suitable tile for resource placement.")

            grid[x][y] = resource_placement_fn(x, y, self.size, grid, value)
            self.state_resources[name] = self.state_resources.get(name, 0) + 1

        return self.state_resources

    def transition_state(self) -> ():
        return ActiveState, self.state_resources


class ResetState(WorldState):
    """
    Represents a state where the world is reset, clearing any existing state or data, and preparing for a new round
    or iteration.
    """

    def transition_state(self) -> ():
        return GenerateState, self.state_resources


class ActiveState(WorldState):
    """
    Represents a state where the world is active and performing its normal operations.
    """
