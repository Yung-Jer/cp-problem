import collections

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if initial point is unwalkable(ie. == 1), return -1
        if grid[0][0] != 0:
            return -1
        
        # Initialize the directions
        direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        n = len(grid)
        # Initialize the queue
        q = collections.deque()
        # Initialize the visited set
        visited = [[0]*n for i in range(n)]
        # Queue storing (x-coordinate, y-coordinate, current path length)
        q.append((0,0,1))
        
        while q:
            curr = q.popleft()
            # If the coordinate is out of bound
            if curr[0] < 0 or curr[1] < 0 or curr[0] >= n or curr[1] >= n:
                continue
            # If the coordinate has been visited
            elif visited[curr[0]][curr[1]]:
                continue
            # If the coordinate is unwalkable (i.e. == 1)
            elif grid[curr[0]][curr[1]]:
                continue
            # If the coordinate is the destination
            elif curr[0] == n-1 and curr[1] == n-1:
                return curr[2]
            else:
                visited[curr[0]][curr[1]] = 1
                for i in range(8):
                    q.append((curr[0]+direction[i][0], curr[1]+direction[i][1], curr[2]+1))
        
        # if the queue is empty and you have not reached the last point, return -1
        return -1