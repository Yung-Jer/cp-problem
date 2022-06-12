import re, collections

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: list[list[str]]) -> bool:
        map_func = collections.defaultdict(set)
        for old, new in mappings:
            map_func[old].add(new)
        for char in sub:
            map_func[char].add(char)
        
        regex = ""
        for char in sub:
            temp = []
            temp.append(regex)
            if len(map_func[char]) > 1:
                temp.append('(')
                temp.append('|'.join(map_func[char]))
                temp.append(')')
            else:
                temp.append(char)
            regex = ''.join(temp)
        return bool(re.compile(regex).search(s))

# Credit to Leetcode user: https://leetcode.com/theabbie/
# Refer from: https://leetcode.com/problems/match-substring-after-replacement/discuss/2138774/Using-Regex