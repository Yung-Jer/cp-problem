class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        def partition(l, r, pivot):
            p = nums[pivot]
            nums[r], nums[pivot] = nums[pivot], nums[r]
            
            curr = l
            for i in range(l, r):
                if nums[i] < p:
                    nums[i], nums[curr] = nums[curr], nums[i]
                    curr += 1
            nums[curr], nums[r] = nums[r], nums[curr]
            return curr
        
        def quick_select(l, r, k_idx):
            if l == r:
                return nums[l]
            
            pivot_idx = partition(l, r, l)
            
            if pivot_idx == k_idx:
                return nums[pivot_idx]
            
            elif k_idx < pivot_idx:
                return quick_select(l, pivot_idx-1, k_idx)
            else:
                return quick_select(pivot_idx+1, r, k_idx)
        
        return quick_select(0, n-1, n-k)