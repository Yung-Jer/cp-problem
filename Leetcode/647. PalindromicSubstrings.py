class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def recur(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        # recur(i, i) is for case like aba, recur(i, i+1) is for case like abba
        return sum(recur(i, i) + recur(i, i+1) for i in range(len(s))) 