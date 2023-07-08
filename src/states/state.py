class State:
    """
    Defines the behavior of the system
    """
    def __init__(self, name):
        """
        Defines the name of this state for retrieval ana analysis.
        Also stores any relevant information about the state, e.g, agent location, world resources, etc...
        :param name:
        """
        self.name = name

    def perform_action(self):
        """
        Performs the primary action defined when object is in this state.
        :return: The object after performing the action.
        """
        pass

    def perform_utility_action(self):
        """
        Performs the supporting action when object is in this state.
        :return: The affected object after performing the action.
        """
        pass

    def transition_state(self):
        """
        Determines what state the object should be in based on current information.
        :return: The next state based on data.
        """
        pass
