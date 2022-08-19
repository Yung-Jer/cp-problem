from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        cnt = Counter(nums)
        end = defaultdict(int)
        
        for i in nums:
            if cnt[i]:
                cnt[i] -= 1
                
                if end[i - 1]:
                    end[i - 1] -= 1
                    end[i] += 1
                    
                elif cnt[i + 1] and cnt[i + 2]:
                    cnt[i + 1] -= 1
                    cnt[i + 2] -= 1
                    end[i + 2] += 1
                else:
                    return False
        return True