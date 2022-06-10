class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def privatefunc(prev, target, combi):
            if target == 0 and len(combi) == k:
                res.append(combi)
                return
            elif target < 0 or len(combi) >= k:
                return
            else:
                # We only start from previous number + 1 to avoid repetition, this will allows numbers in combination 
                # to be in ascending order
                for i in range (prev+1, 10):
                    privatefunc(i, target - i, combi + [i])
                    
        #start from 0 as previous number (as a dummy)            
        privatefunc(0, n, [])
        return res
        