import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return collections.Counter(magazine) >= collections.Counter(ransomNote)