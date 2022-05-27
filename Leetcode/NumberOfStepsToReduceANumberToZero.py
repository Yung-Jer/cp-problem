class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        count = 0
        while num > 0:
            if num % 2 == 1:
                count += 1
            num = num >> 1
            count += 1
        return count - 1 # subtract away when num == 1, we add count by 1 after doing right shift