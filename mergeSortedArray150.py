class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        x, y = 0, 0
        z = 0
        numsCopy = nums1.copy()
        while x < m and y < n:
            if numsCopy[x] <= nums2[y]:
                nums1[z] = numsCopy[x]
                x += 1
            else:
                nums1[z] = nums2[y]
                y += 1
            z += 1
        
        if y < n:
            for i in range(y, n):
                nums1[z] = nums2[i]
                z += 1
        elif x < m:
            for i in range(x, m):
                nums1[z] = numsCopy[i]
                z += 1
                
                # Runtime 43ms Beats 90.73% // Memory 16.5MB Beats 14.47%
