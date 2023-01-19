class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def checker(word):
            res = []
            check = {}
            swaps = 0
            for i in word:
                if i not in check:
                    check[i] = swaps
                    swaps += 1
                res.append(check[i])
            return res

        return checker(s) == checker(t)
      
# Runtime: 32ms Beats 97.59% 
# Memory: 14.6MB Beats 12.3%
