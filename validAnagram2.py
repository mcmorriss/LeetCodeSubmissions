# Michael Morriss
# 9/16/2022
# Valid Anagram Submission 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for item in s:
            if item in letters:
                letters[item] += 1
            else:
                letters[item] = 1
        for item in t:
            if item in letters:
                letters[item] -= 1
            else:
                return False
        for x in letters.values():
            if x != 0:
                return False
        return True
      
# Runtime: 72 ms, faster than 61.20% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 26.77% of Python3 online submissions for Valid Anagram.
