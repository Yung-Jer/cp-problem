# by counting the number of set bits at each corresponding bits position for all array elements 
# and then the maximum count of set bits at any position is the maximum count of subset 
# required because the Bitwise AND of all those elements is always positive.

class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        # Initialize a super large set bits array
        # Store the number of set bits at each bit position
        bit = [0] * 32
        
        for i in range(len(candidates)):
            # starting from the last set bit (last set bit)
            x = 31
            while candidates[i] > 0:
                if (candidates[i] & 1 == 1):
                    bit[x] += 1
                # right shift the number by 1 (number divided by 2)
                candidates[i] = candidates[i] >> 1
                x -= 1
        return max(bit)