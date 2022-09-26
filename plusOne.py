# Date: September 26th, 2022

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits) - 1
        while x > 0:
            if digits[x] == 9:
                digits[x] = 0
                x -= 1
            else:
                digits[x] += 1
                return digits
        if digits[x] == 9:
            digits[x] = 0
            digits.insert(0, 1)
        else:
            digits[x] += 1
        return digits
        
        # Runtime: 76 ms, faster than 5.35% of Python3 online submissions for Plus One.
        # Memory Usage: 14 MB, less than 12.18% of Python3 online submissions for Plus One.
