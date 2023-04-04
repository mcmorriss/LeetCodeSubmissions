class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        lowest = 10001
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > maxVal:
                maxVal = prices[i] - lowest
        return maxVal
