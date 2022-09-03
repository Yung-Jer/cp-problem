class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        ans = []
        
        def dfs(num):
            if len(num) == n:
                ans.append(int(''.join(num)))
                return
            i = int(num[-1])
            if k == 0:
                dfs(num + [str(i)])
            else:
                if (i + k) <= 9:
                    dfs(num + [str(i + k)])
                if (i - k) >= 0:
                    dfs(num + [str(i - k)])
                    
        for i in range(1,10):
            dfs([str(i)])
        return ans