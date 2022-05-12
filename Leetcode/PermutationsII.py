## Using DFS concept

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dct = {}
        
        def dfs(path, visited):
            if len(path) == len(nums):
                a = ''
                for i in range(len(path)):
                    a += str(path[i])
                if dct.get(a, 0) == 0:
                    dct[a] = 1
                    res.append(path)
                return

            for i in range(len(visited)):
                if visited[i] == 0:
                    new_visited = visited[:]
                    new_visited[i] = 1
                    new_path = path[:]
                    new_path.append(nums[i])
                    dfs(new_path, new_visited)
        dfs([], [0]*len(nums))
        return res