class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])
        p_set = set()
        a_set = set()
        
        def dfs(i, j, which_set):
            which_set.add((i, j))
            drec = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
            for dx, dy in drec:
                new_i, new_j = i + dx, j + dy
                # we are actually backtracking from the edge, hence we want to find the inverse relationship
                # i.e. heights[i][j] <= heights[new_i][new_j], which means that the water can flow from the
                # new coordinates to the current one
                if 0 <= new_i < m and 0 <= new_j < n and heights[i][j] <= heights[new_i][new_j] and (new_i, new_j) not in which_set:
                    dfs(new_i, new_j, which_set)
                    
        for i in range(n):
            dfs(0, i, p_set)
            dfs(m-1, i, a_set)
            
        for i in range(m):
            dfs(i, 0, p_set)
            dfs(i, n-1, a_set)
            
        return list(p_set & a_set)