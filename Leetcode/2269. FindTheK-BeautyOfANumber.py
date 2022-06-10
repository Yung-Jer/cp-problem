class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        i = 0
        cnt = 0
        num_str = str(num)
        while (i + k - 1) < len(num_str):
            substr = num_str[i:i+k]
            if int(substr) != 0 and num % int(substr) == 0:
                cnt+=1
            i+=1
        return cnt