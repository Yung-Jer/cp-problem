class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        res = [1] * n
        
        if n > 1 and ratings[0] > ratings[1]:
            res[0] += 1
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1] + 1

        return sum(res)
