from unittest import TestCase
from unittest.mock import patch

from src.worlds.world import World


class TestWorld(TestCase):
    def test_generate(self):
        world = World(3)
        expected_result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        with patch('random.choice', return_value=1):
            result = world.generate()
        self.assertEqual(result, expected_result)
