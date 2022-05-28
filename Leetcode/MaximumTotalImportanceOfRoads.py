import collections

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        g = collections.defaultdict(list)
        for u,v in roads:
            g[u].append(v)
            g[v].append(u)
        
        roads2 = []
        for i in g:
            roads2.append([i, len(g[i])])
        roads2.sort(key=lambda x:x[1], reverse = True)
        dct = {}
        for i in range(len(roads2)):
            dct[roads2[i][0]] = n - i
        ans = 0
        for i in roads:
            ans += dct[i[0]] + dct[i[1]]
            
        return ans