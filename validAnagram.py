# Michael Morriss
# Date: 9/16/2022
# 242: Valid Anagram (https://leetcode.com/problems/valid-anagram/)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_sort = sorted(t)
        return s_sort == t_sort
      
      
#Runtime: 103 ms, faster than 21.72% of Python3 online submissions for Valid Anagram.
#Memory Usage: 15.1 MB, less than 21.76% of Python3 online submissions for Valid Anagram.#
