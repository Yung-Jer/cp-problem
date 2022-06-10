import collections

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
        if grid[0][0] == ")":
            return False
        
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        dct = set()
        
        dct.add((0,0,0))
        q.append((0,0,0))
        flag = False
        
        while q:
            x,y,count = q.popleft()
            if grid[x][y] == "(":
                count += 1
            else:
                count -= 1

            if x == m-1 and y == n-1 and count == 0:
                flag = True
                break

            if count >=0:
                for newx, newy in [(x,y+1), (x+1,y)]:
                    if newx < m and newy < n and (newx,newy,count) not in dct:
                        q.append((newx,newy,count))
                        dct.add((newx,newy,count))
        return flag