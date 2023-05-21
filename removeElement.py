class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        x = 0
        end = len(nums)
        while x < end:
            if nums[x] == val:
                nums.pop(x)
                end -= 1
            else:
                x += 1
        return len(nums)
