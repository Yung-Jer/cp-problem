# We have to use a stack to solve the problem in O(N) time complexity.
# Instead of spending more time checking the previous k elements are the same, we store [char, counter] in the stack
# to keep track of the count of the last element

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in list(s):
            if len(stack) != 0 and stack[-1][0] == i:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i, 1])
        ans = ''
        for i, count in stack:
            ans += i*count
        return ans