class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        stack = []
        stack.append(words[0])
        
        for i in range(1, len(words)):
            top = stack[-1]
            if sorted(words[i]) == sorted(top):
                continue
            else:
                stack.append(words[i])
        return stack