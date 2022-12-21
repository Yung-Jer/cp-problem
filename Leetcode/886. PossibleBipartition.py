from collections import deque, defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = defaultdict(list)

        for i, j in dislikes:
            g[i-1].append(j-1)
            g[j-1].append(i-1)

        visited = [0] * n
        q = deque()

        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                q.append(i)

                while q:
                    for i in range(len(q)):
                        u = q.pop()
                        for k in range(len(g[u])):
                            if not visited[g[u][k]]:
                                visited[g[u][k]] = 2 if visited[u] == 1 else 1
                                q.append(g[u][k])
                            
                            if visited[u] == visited[g[u][k]]:
                                return False
            
        return True
                    