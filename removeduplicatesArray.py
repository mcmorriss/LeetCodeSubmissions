# September 12th, 2022

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                k -= 1
                nums.pop(i)
        return k
         
         # Runtime: 208 ms, faster than 19.92% of Python3 online submissions for Remove Duplicates from Sorted Array.
         # Memory Usage: 15.7 MB, less than 19.29% of Python3 online submissions for Remove Duplicates from Sorted Array.
         # https://leetcode.com/problems/remove-duplicates-from-sorted-array
