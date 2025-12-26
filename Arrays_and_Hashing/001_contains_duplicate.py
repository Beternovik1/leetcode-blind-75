"""
PROBLEM: Contains Duplicate
LINK: https://neetcode.io/problems/duplicate-integer/question
DIFFICULTY:Easy
TAGS: Arrays, Hashing

DESCRIPTION: Given an integer array nums, return true if any value appears more than once 
in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]

Output: true

Example 2:
Input: nums = [1, 2, 3, 4]

Output: false
"""

"""
Complexity
certain terms "dominate" others
O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!)
"""

from typing import List

class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def brute_force(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # Time: O(nlogn)
    # Space: O(1)
    def sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

    # Time: O(n)
    # Space: O(n)
    def hash_set(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
    # Time: O(n)
    # Space: O(n)
    def hash_set_length(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    
if __name__ == "__main__":
    # Creating the object
    solver = Solution()

    # Defining the test cases
    test_case_1 = [1, 2, 3, 3]
    test_case_2 = [1, 2, 3, 4]
    
    # Run the tests
    print(f"Test 1 (Expected True):  {solver.hash_set(test_case_1)}")
    print(f"Test 2 (Expected False):  {solver.hash_set(test_case_2)}")

