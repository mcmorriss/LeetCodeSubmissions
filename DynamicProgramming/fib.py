class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        sums = [0] * (n + 1)
        sums[1] = 1
        for i in range(2, n + 1):
            sums[i] = sums[i - 1] + sums[i - 2]
        return sums[n]
