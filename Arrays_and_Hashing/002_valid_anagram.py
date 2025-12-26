"""
PROBLEM: Valid Anagram
LINK: https://neetcode.io/problems/is-anagram/question?list=blind75
DIFFICULTY:Easy
TAGS: Arrays, Hashing

DESCRIPTION: Given two strings s and t, return true if the two strings are anagrams 
of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"

Output: true

Example 2:
Input: s = "jar", t = "jam"

Output: false

Constraints:
s and t consist of lowercase English letters.
"""
from collections import Counter

class Solution:
    def sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    
    def hash_tables(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t
    
    def hash_tables_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True
    
    def hash_tables_3(self, s: str, t:str) -> bool:
        # counter is a data structure in python that is a hashmap but 
        # it count things automaticly
        return Counter(s) == Counter(t)
    
    def hash_table_using_array(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        for i in range(len(s)):
            # ord is ordinal and is a boult-in python fuction
            # that takes a single character and return its 
            # integer ID from ASCII or Unicode number
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
    

if __name__ == '__main__':
    solver = Solution()

    s1 = 'racecar'
    t1 = 'carrace'

    s2 = 'jar'
    t2 = 'jam'

    print(f'Expected (True) {solver.hash_table_using_array(s1, t1)}')
    print(f'Expected (False) {solver.hash_table_using_array(s2, t2)}')

