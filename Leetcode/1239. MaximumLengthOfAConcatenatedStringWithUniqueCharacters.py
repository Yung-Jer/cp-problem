class Solution:
    def maxLength(self, arr: "list[str]") -> int:
        res = [""]
        ans = 0
        
        for i in arr:
            for combi in res:
                new_w = i + combi
                if len(new_w) != len(set(new_w)):
                    continue
                res.append(new_w)
                ans = max(ans, len(new_w))
        return ans

