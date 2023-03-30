class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = False
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        ans = ""

        while p2 >= 0:
            if carry:
                tempSum = 1
                carry = False
            else:
                tempSum = 0

            tempSum += (int(num1[p1]) + int(num2[p2]))

            if tempSum > 9:
                carry = True
                tempSum -= 10
            ans = str(tempSum) + ans
            
            p1 -= 1
            p2 -= 1

        while p1 >= 0:
            if carry:
                tempSum = 1
                carry = False
            else:
                tempSum = 0

            tempSum += int(num1[p1])

            if tempSum > 9:
                carry = True
                tempSum -= 10
            ans = str(tempSum) + ans

            p1 -= 1
        
        if carry:
            ans = "1" + ans



        return ans
