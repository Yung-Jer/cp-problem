class UnionFind:
    def __init__(self, n):
        self.p = []
        self.rank = [0] * n
        
        for i in range(0, n):
            self.p.append(i)
            
    def findSet(self,n):
        if self.p[n] == n:
            return n
        else:
            self.p[n] = self.findSet(self.p[n])
            return self.p[n]

    def isSameSet(self, n, m):
        return self.findSet(n) == self.findSet(m)

    def unionSet(self, n, m):
        if not (self.isSameSet(n,m)):
            x = self.findSet(n)
            y = self.findSet(m)

            if (self.rank[x] > self.rank[y]):
                self.p[y] = x

            else:
                self.p[x] = y
                if (self.rank[x] == self.rank[y]):
                    self.rank[y] += 1
                    
class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        base = ord('a')
        uf = UnionFind(26)
        equations.sort(key = lambda x: x[1], reverse = True)
        
        for e in equations:
            x = e[0]
            y = e[-1]
            if e[1] == "=":
                uf.unionSet(ord(x)-base, ord(y)-base)
            else:
                if uf.isSameSet(ord(x)-base, ord(y)-base):
                    return False
        return True