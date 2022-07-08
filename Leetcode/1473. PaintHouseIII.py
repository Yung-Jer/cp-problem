class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        _seen = {}
        
        def dp(index, target, prev):
            if (index, target, prev) in _seen:
                return _seen[(index, target, prev)]
            # target > m - index: remaining house < remaining neighbor to form
            elif target < 0 or target > m - index:
                return 10000000000
            # all houses are painted
            elif index == m:
                return 0
            # houses painted
            elif houses[index]:
                _seen[(index, target, prev)] = dp(index+1, target - (prev != houses[index]), houses[index])
                return _seen[(index, target, prev)]
            # if target is already reached, just paint all the following houses with the previous color
            elif target == 0:
                _seen[(index, target, prev)] = cost[index][prev-1] + dp(index+1, target, prev)
                return _seen[(index, target, prev)]
            else:
                ans = 10000000000
                # try every paint color
                for paint in range(n):
                    ans = min(ans, cost[index][paint] + dp(index+1, target - (prev != paint+1), paint+1))
                _seen[(index, target, prev)] = ans
                return ans
        ans = dp(0, target, -1)
        return ans if ans < 10000000000 else -1