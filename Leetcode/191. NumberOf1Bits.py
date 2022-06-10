class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0b0000000000000000000000000001011 = 11, 0b prefix indicates binary number
        # 0b0000000000000000000000000000011 & 1 << 1 = 2
        # 0b0000000000000000000000000000011 & 1 << 2 = 4
        # 0b0000000000000000000000000000111 & 1 << 3 = 0
        return sum((n & 1 << i) != 0 for i in range(32))