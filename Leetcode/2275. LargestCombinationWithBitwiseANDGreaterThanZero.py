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
                    # the count of set bits at the corresponding bit position
                    # indicating that there are n elements with set bit at the same bit position
                    # hence it shows that the Bitwise AND for all these n elements is always positive at this bit position 
                    bit[x] += 1
                # right shift the number by 1 (number divided by 2)
                candidates[i] = candidates[i] >> 1
                x -= 1
        # Return the maximum count of set bits at any position since the Bitwise AND of the n elements at this bit position 
        # will be always positive (non-zero)
        return max(bit)