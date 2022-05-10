## Works but TLE

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        
        if grid[0][0] == ")":
            return False
        queue = []
        queue.append([ (0,0), [grid[0][0]] ])
        flag = False
        
        while queue:
            temp = queue.pop(0)
            if temp[0] == (len(grid)-1, len(grid[0])-1) and len(temp[1]) == 0:
                flag = True
                break
            if temp[0][0] + 1 < len(grid):
                nxt = grid[temp[0][0]+1][temp[0][1]]
                stack = temp[1][:]
                if len(stack) > 0 and stack[-1] == "(" and nxt == ")":
                    stack.pop()
                else:
                    stack.append(nxt)
                queue.append([(temp[0][0]+1, temp[0][1]), stack])
            if temp[0][1] + 1 < len(grid[0]):
                nxt = grid[temp[0][0]][temp[0][1]+1]
                stack = temp[1][:]
                if len(stack) > 0 and stack[-1] == "(" and nxt == ")":
                    stack.pop()
                else:
                    stack.append(nxt)
                queue.append([(temp[0][0], temp[0][1]+1), stack])
        return flag