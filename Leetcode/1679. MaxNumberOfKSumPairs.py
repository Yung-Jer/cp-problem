class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dct = {}
        for i in range(len(nums)):
            a = dct.get(nums[i], -1)
            if a == -1:
                dct[nums[i]] = 1
            else:
                dct[nums[i]] = a + 1
        
        counter = 0
        for i in dct.keys():
            b = dct.get(k - i, -1)
            if b == -1:
                continue
            elif i == k - i:
                numpairs = dct[i] // 2
                dct[i] -= numpairs*2
                counter += numpairs
            else:
                minpair = min(dct[i], dct[k-i])
                dct[i] -= minpair
                dct[k-i] -= minpair
                counter += minpair
        return counter