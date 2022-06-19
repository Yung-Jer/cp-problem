class Solution:
    def greatestLetter(self, s: str) -> str:
        _seen = set()
        res = ""
        
        for i in s:
            _seen.add(i)
        
        for i in _seen:
            if i.islower() and i.upper() in _seen:
                res = max(res, i.upper())
        return res