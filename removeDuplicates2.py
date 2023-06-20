class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        newLen = len(nums)
        while x + 2 < newLen:
            if nums[x] == nums[x+2]:
                nums.pop(x)
                newLen -= 1
            else:
                x += 1
        return newLen
      
      # Runtime 74 ms Beats 34.75% // Memory 16.2 MB Beats 87.34%
