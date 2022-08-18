from collections import Counter

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        n = len(arr)
        target = n // 2
        key_count = sorted(Counter(arr).values(), reverse = True)
        counter = 0
        
        for i in key_count:
            counter += 1
            n -= i
            if n <= target:
                return counter