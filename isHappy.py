# Date: December 12th, 2022

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {n}
        while True:
            total = 0
            for i in str(n):
                total += int(i) ** 2
            if total == 1:
                return True
            if total in nums:
                return False
            nums.add(total)
            n = total
            
            # Runtime: 67 ms, faster than 33.38% of Python3 online submissions for Happy Number.
            # Memory Usage: 13.8 MB, less than 96.79% of Python3 online submissions for Happy Number.
