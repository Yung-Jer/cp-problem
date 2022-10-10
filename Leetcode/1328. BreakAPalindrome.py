class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        temp = list(palindrome)
        idx = -1
        for i in range(len(temp) // 2):
            if temp[i] != 'a':
                idx = i
                break
        temp[idx] = 'a' if idx != -1 else 'b'
        return ''.join(temp)