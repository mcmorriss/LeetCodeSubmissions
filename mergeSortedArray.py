# September 23rd 2022

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        i, j, k = 0, 0, 0
        
        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < m:
            nums1[k] = temp[i]
            i += 1
            k += 1
        
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
            
            # Runtime: 68 ms, faster than 39.94% of Python3 online submissions for Merge Sorted Array.
            # Memory Usage: 14 MB, less than 38.10% of Python3 online submissions for Merge Sorted Array.
            # https://leetcode.com/problems/merge-sorted-array
