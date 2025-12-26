"""
PROBLEM: Valid Anagram
LINK: https://neetcode.io/problems/two-integer-sum/question?list=blind75
DIFFICULTY:Easy
TAGS: Arrays, Hashing

DESCRIPTION: Given an array of integers nums and an integer target, return the indices i and j
such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy 
the condition.

Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10

Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10

Output: [0,1]

Constraints:
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:            
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
                
    def hash_map(self, nums:List[int], target:int) -> List[int]:
        hash_map = {} # val : index

        for i, num in enumerate(nums):
            difference = target - num
            if difference in hash_map:
                return [hash_map[difference], i]
            hash_map[num] = i
        return None
        

if __name__ == '__main__':
    solver = Solution()

    nums1 = [3,4,5,6]
    target1 = 7
    nums2 = [4,5,6]
    target2 = 10
    nums3 = [5,5]
    target3 = 10


    print(f'Expected[0,1]: {solver.hash_map(nums1, target1)}')
    print(f'Expected[0,2]: {solver.hash_map(nums2, target2)}')
    print(f'Expected[0,1]: {solver.hash_map(nums3, target3)}')


