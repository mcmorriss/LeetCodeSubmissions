# Date: September 26th, 2022

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        x = len(s) - 1
        while x >= 0:
            if s[x] == ' ':
                if length == 0:
                    x -= 1
                    continue
                else:
                    return length
            length += 1
            x -= 1
        return length
      
      # Runtime: 68 ms, faster than 6.71% of Python3 online submissions for Length of Last Word.
      # Memory Usage: 14 MB, less than 5.61% of Python3 online submissions for Length of Last Word.
