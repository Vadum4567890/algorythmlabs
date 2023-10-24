import unittest

def two_sum(nums, target):
    num_dict = {}
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            result.append([num_dict[complement], i])
        num_dict[num] = i
    return result if result else -1



class TestTwoSum(unittest.TestCase):

    def test_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_example2(self):
        nums = [3, 2, 4]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, [1, 2])

    def test_example3(self):
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_example4(self):
        nums = [3, 5]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, -1)


    nums = [5, 4, 11, 15, 7, 2, 8,1]
    target = 9
    result = two_sum(nums, target)
    print(result)