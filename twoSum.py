class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[nums[i]] = i
