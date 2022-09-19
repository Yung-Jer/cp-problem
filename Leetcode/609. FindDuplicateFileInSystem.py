import collections

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        _seen = collections.defaultdict(list)
        
        for i in paths:
            temp = i.split(' ')
            path = temp[0]
            for j in range(1, len(temp)):
                left = temp[j].find('(')
                right = temp[j].find(')')
                _seen[temp[j][left+1: right]].append(path + '/' + temp[j][:left])
        return [i for i in list(_seen.values()) if len(i) > 1]