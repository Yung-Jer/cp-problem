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

class Solution2(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary_str = bin(num)
         # binary string starts with 0b, so minus 2
         # when num == 1, we just subtract by 1 and bitshift to the right by 1 is not needed, so minus 1 here
         # In total minus 3
        return len(binary_str) + binary_str.count('1') - 3