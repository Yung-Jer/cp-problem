import collections

class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 == 1:
            return []
        changed.sort()
        q = collections.deque()
        res = []
        for i in changed:
            if q and q[0] * 2 == i:
                res.append(q.popleft())
            else:
                q.append(i)
        return res if not q else []