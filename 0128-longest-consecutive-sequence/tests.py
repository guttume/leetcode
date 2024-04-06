
import random
import unittest

from main import Solution


class LongestConsecutiveSequenceTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        self.s = Solution()
        super().__init__(methodName)

    def test_sample_one(self):
        nums = [100,4,200,1,3,2]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 4)

    def test_sample_two(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 9)
        
    def test_single_element(self):
        nums = [6]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 1)
        
    def test_positive_numbers(self):
        nums = [152, 6, 9, 8, 7, 25]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 4)
        
    def test_negative_numbers(self):
        nums = [-4, -3, -2, -1, 0, 1, 2]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 7)
        
    def test_same_elements(self):
        nums = [3, 3, 3, 3, 3]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 1)
        
    def test_with_duplicates(self):
        nums = [3, 100, 4, 100, 200, 1, 3, 2, 4]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 4)
        
    def test_with_gaps(self):
        nums = [5, 7, 9, 11, 13, 15]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 1)
        
    def test_mixed_sequence(self):
        nums = [-2, 0, 4, -1, 2, 3, -3]
        self.assertEqual(self.s.longestConsecutive(nums=nums), 4)
        
    def test_large_list(self):
        random.seed(42)
        nums = list(range(10**5))
        random.shuffle(nums)
        random.seed(42)
        nums.extend(random.choices(range(10**5), k=10**5))
        random.shuffle(nums)
        self.assertEqual(self.s.longestConsecutive(nums=nums), 100000)
        

if __name__ == "__main__":
    unittest.main()