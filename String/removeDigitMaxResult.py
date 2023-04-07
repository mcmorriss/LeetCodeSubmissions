class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxNum = -1
        p1, p2 = 0, len(number) - 1
        while p1 <= p2:
            if number[p1] == digit:
                temp = list(number)
                temp.pop(p1)
                "".join(temp)
                check = int("".join(temp))
                if check > maxNum:
                    maxNum = check
            if number[p2] == digit:
                temp = list(number)
                temp.pop(p2)
                check = int("".join(temp))
                if check > maxNum:
                    maxNum = check
            p1 += 1
            p2 -= 1
        return str(maxNum)
