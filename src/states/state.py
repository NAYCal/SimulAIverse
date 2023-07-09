class State:
    """
    Defines the behavior of the system
    """
    def __init__(self, name, *args):
        """
        Defines the name of this state for retrieval ana analysis.
        Also stores any relevant information about the state, e.g, agent location, world resources, etc...
        :param name:
        """
        self.name = name

    def perform_action(self, *args) -> {}:
        """
        Performs the primary action defined when object is in this state.
        :param args: Other arguments helpful to performing the action.
        :return: A map of changed properties after performing the action.
        """
        pass

    def perform_utility_action(self, *args) -> {}:
        """
        Performs the supporting action when object is in this state.
        :param args: Other arguments helpful to performing the action.
        :return: A map of what is done in the particular state, e.g. resource changes at the tile,
        """
        pass

    def transition_state(self) -> ():
        """
        Determines what state the object should be in based on current information, and pass down any relevant
        information to the next state.
        :return: A tuple where the first object is the name of the next state based on data, and other properties to be
        passed.
        """
        pass
