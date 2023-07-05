import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from src.models.model import Model
from src.states.state import State


class TestModelInterface(TestCase):
    def setUp(self) -> None:
        self.model = Model()

    def test_next(self):
        # Create mock state objects
        start_state = MagicMock(spec=State)
        end_state = MagicMock(spec=State)
        intermediate_state = MagicMock(spec=State)

        # Configure the mock state objects to simulate the desired behavior
        start_state.is_end_state.return_value = False
        start_state.get_valid_states.return_value = [intermediate_state]
        intermediate_state.is_end_state.return_value = False
        intermediate_state.get_valid_states.return_value = [end_state]
        end_state.is_end_state.return_value = True
        end_state.get_valid_states.return_value = []

        # Define the expected path
        expected_path = [start_state, intermediate_state, end_state]

        # Call the next method on the model
        result = self.model.next(start_state)

        # Assert that the result matches the expected path
        self.assertEqual(result, expected_path)

    def test_iterator(self):
        # Create mock state objects
        start_state = MagicMock(spec=State)
        end_state = MagicMock(spec=State)
        intermediate_state = MagicMock(spec=State)

        # Configure the mock state objects to simulate the desired behavior
        start_state.is_end_state.return_value = False
        start_state.get_valid_states.return_value = [intermediate_state]
        intermediate_state.is_end_state.return_value = False
        intermediate_state.get_valid_states.return_value = [end_state]
        end_state.is_end_state.return_value = True
        end_state.get_valid_states.return_value = []

        # Define the expected path
        expected_path = [start_state, intermediate_state, end_state]

        # Get the iterator from the model
        self.model.next(start_state)
        iterator = iter(self.model)

        # Convert the iterator to a list and compare with the expected path
        self.assertEqual(list(iterator), expected_path)


if __name__ == "__main__":
    # Run the tests
    unittest.main()
