from bisect import bisect_left
class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        properties.sort(key = lambda x: (-x[0], x[1]))
        n = len(properties)
        max_atk = properties[0][0]
        max_def = properties[0][1]
        
        cnt = 0
        for i in range(1, n):
            if max_atk > properties[i][0] and max_def > properties[i][1]:
                cnt += 1
            else:
                max_atk, max_def = properties[i]
        return cnt