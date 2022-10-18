class Solution:
    def countAndSay(self, n: int) -> str:
        def recur(n):
            if n == 1:
                return "1"
            else:
                num = recur(n-1)
                stack = [["#", 1]]
                for i in str(num):
                    if i == stack[-1][0]:
                         stack[-1][1] +=1 
                    else:
                         stack.append([i, 1])
                string = ''.join([str(num) + char for char, num in stack])
                return string[2:]
        return recur(n)