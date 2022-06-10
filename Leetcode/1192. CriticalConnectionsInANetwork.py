import collections

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        '''
        u --> The vertex to be visited next
        visited[] --> keeps track of visited vertices
        discTime[] --> Stores discovery times (first meet times) of visited vertices
        parent[] --> Stores parent vertices in DFS tree
        rank[] ---> Stores rank of vertices, i.e. vertices of a same cycle will share the same rank
        '''
        visited = [0] * n
        discTime = [1000000] * n
        rank = [1000000] * n
        parent = [-1] * n
        self.t = 1
        res = []
        
        def bridgeDfs(u):
            discTime[u] = self.t
            rank[u] = self.t
            visited[u] = 1
            self.t += 1
            
            for v in graph[u]:
                if v == parent[u]:
                    continue
                elif not visited[v]:
                    parent[v] = u
                    bridgeDfs(v)
                rank[u] = min(rank[u], rank[v])
                if discTime[u] < rank[v]:
                    res.append([u, v])
        
        bridgeDfs(0)
        return res