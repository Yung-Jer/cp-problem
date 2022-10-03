class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        l, r = -1, -1
        _sum = 0
        _max = float('-inf')
        colors += '#'
        neededTime += [0]
        n = len(colors)
        prev = '#'
        res = 0
        
        for i in range(n):
            if colors[i] != prev and l != r:
                res += (_sum - _max)
                l = i
                r = i
                _sum = neededTime[i]
                _max = neededTime[i]
            elif colors[i] != prev:
                l += 1
                r += 1
                _sum = neededTime[i]
                _max = neededTime[i]
            else:
                r += 1
                _sum += neededTime[i]
                _max = max(_max, neededTime[i])
            prev = colors[i]
        return res