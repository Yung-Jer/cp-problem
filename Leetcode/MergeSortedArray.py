class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointA = 0
        pointB = 0
        idx = 0
        
        temp = nums1[:m]
        
        while pointA < m and pointB < n:
            if temp[pointA] <= nums2[pointB]:
                nums1[idx] = temp[pointA]
                pointA += 1
            else:
                nums1[idx] = nums2[pointB]
                pointB += 1
            
            idx += 1
            
        rem_point = pointB if pointA >= m else pointA
        rem_list = nums2 if pointA >= m else temp
        
        for i in range(idx, m+n):
            nums1[i] = rem_list[rem_point]
            rem_point += 1