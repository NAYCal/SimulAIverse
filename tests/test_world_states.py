from unittest import TestCase
from unittest.mock import MagicMock

from src.containers.container import Container
from src.states.world_states import GenerateState


def create_mock_container(name, x, y, value):
    container_mock = MagicMock()
    container_mock.name = name
    container_mock.x_coord = x
    container_mock.y_coord = y
    container_mock.value = value

    # Modify the mock object to behave like an instance of the Container class
    container_mock.__class__ = Container

    return container_mock


class TestGenerateState(TestCase):
    def test_perform_action(self):
        state = GenerateState("Test GenerateState", {})
        result = state.perform_action()

        self.assertEqual(len(result), state.size)
        for row in result:
            self.assertEqual(len(row), state.size)

    def test_perform_utility_action_no_container(self):
        state = GenerateState("Test GenerateState", {})
        expected_result = {"fruit": 1, "fly": 1}
        grid = state.perform_action()

        input_state_resources = {"fruit": 0, "fly": 1}
        test_result = state.perform_utility_action(input_state_resources)

    def test_perform_utility_action_with_container(self):
        state = GenerateState("Test GenerateState", {})
        grid = state.perform_action()

    def test_transition_state(self):
        self.fail()
