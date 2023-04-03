class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0

        if len(nums) == 1:
            return 1

        while x != len(nums) - 1:
            if nums[x] == nums[x + 1]:
                nums.pop(x)
            else:
                x += 1
        return len(nums)
