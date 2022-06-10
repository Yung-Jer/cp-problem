import collections

# The idea is to do dijkstra's algorithm to find the shortest path from the source to the destination
# However, since we only sort the priority queue by 0 weight or non-zero weight, it is okay to use a deque instead of heapq
# Process all the 0 edges first (which will not increase the cost), then all the 1 edges
# Append 0 edges to the left of the deque, append 1 edges to the right of the deque
# This method is called 0-1 BFS

class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        D = [[1000000] * n for i in range(m)]
        
        q = collections.deque()
        # store (dist, row, col) in the deque
        q.append((grid[0][0], 0, 0))
        
        while q:
            for i in range(len(q)):
                # remove the least cost (no. of obstacles required to clear)
                dist, row, col = q.popleft()
                
                for dx, dy in directions:
                    newrow = row + dx
                    newcol = col + dy
                
                    # new coordinates not visited
                    if 0 <= newrow < m and 0 <= newcol < n and D[newrow][newcol] == 1000000:
                        if grid[newrow][newcol] == 1:
                            D[newrow][newcol] = dist + 1
                            q.append((dist+1, newrow, newcol))
                        else:
                            D[newrow][newcol] = dist
                            q.appendleft((dist, newrow, newcol))
        return D[m-1][n-1]