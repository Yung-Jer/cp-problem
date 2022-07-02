class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts = [0] + horizontalCuts
        horizontalCuts.append(h)
        
        verticalCuts.sort()
        verticalCuts = [0] + verticalCuts
        verticalCuts.append(w)
        
        diff1 = 0
        diff2 = 0
        
        for i in range(1, len(horizontalCuts)):
            diff1 = max(diff1, horizontalCuts[i] - horizontalCuts[i-1])
            
        for j in range(1, len(verticalCuts)):
            diff2 = max(diff2, verticalCuts[j] - verticalCuts[j-1])
        
        return (diff1*diff2) % (10**9 + 7)