from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        elif len(bank) == 0:
            return -1
        elif end not in bank:
            return -1
        q = deque([])
        _combi = {"A", "C", "G", "T"}
        bank = set(bank)
        q.append(start)
        cnt = 0
        
        while q:
            cnt += 1
            for i in range(len(q)):
                temp = q.popleft()
                for i in range(8):
                    for letter in _combi:
                        if letter == temp[i]:
                            continue
                        mutate = temp[:i] + letter + temp[i+1:]
                        if mutate == end:
                            return cnt
                        if mutate in bank:
                            q.append(mutate)
        return -1