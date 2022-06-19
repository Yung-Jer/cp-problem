# Greedy approach: O(N)
# start searching from the back of the string, find the minimum length of the substring that is slightly larger than K
# count all the 0 in front of the substring and add (length of the substring - 1) 
# -1 is because we found minimum number that is larger than k, now -1 in length to get smaller or equal to k

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        nums = ""
        for i in range(n-1, -1, -1):
            nums = s[i] + nums
            if int(nums, base=2) > k:
                return s[:i+1].count('0') + len(nums) - 1
        return len(s)
        
# Credit to: https://leetcode.com/yzhao156/
# Refer from: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/discuss/2168190/python-6-lines-or-easy-understanding-or-explained