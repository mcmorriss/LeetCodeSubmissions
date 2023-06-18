class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        x = 0
        while x < len(word1) and x < len(word2):
            res += word1[x]
            res += word2[x]
            x += 1
        if x == len(word1):
            res += word2[x:]
        elif x == len(word2):
            res += word1[x:]
        return res

      # Runtime 48 ms .. Beats 32.33%
