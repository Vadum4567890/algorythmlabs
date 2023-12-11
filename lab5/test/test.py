import unittest

import unittest

from algorythmlabs.algorythmlabs.lab5.src.main import max_experience


class MaxExperienceTest(unittest.TestCase):

    def test_max_experience(self):
        levels = 4
        experience = [[4, 1], [3, 1, 5], [2, 1, 3, 2], [1, 3, 2, 1]]

        expected_result = 12

        result = max_experience(levels, experience)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()