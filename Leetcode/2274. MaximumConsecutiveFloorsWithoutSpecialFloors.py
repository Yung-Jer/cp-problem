class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        len_set = set()
        curr_bottom = bottom
        special.sort()
        
        for i in special:
            len_set.add(i - curr_bottom)
            curr_bottom = i+1
        len_set.add(top - curr_bottom + 1)
        return max(len_set)