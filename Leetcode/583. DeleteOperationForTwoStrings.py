# Initialize two pointers, i and j, one for each string.
# since you do not know deleting word1[i] is better or word2[j] is better, 
# hence you have to do recursion to find min(helper(i+1,j), helper(i,j+1)) 
# you'll prob notice there will be a lot of repetition here as (0,1) => (1,1) or (0,2) and (1,0) => (1,1) or (2,0). 
# Hence we need to do memoization (or DP)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dct = {}
        
        def helper(i, j):
            if i == m or j == n:
                return max(m-i, n-j)
            elif (i, j) in dct:
                return dct[(i, j)]
            elif word1[i] == word2[j]:
                dct[(i, j)] = helper(i+1, j+1)
                return dct[(i, j)]
            else:
                dct[(i, j)] = min(helper(i+1, j), helper(i, j+1)) + 1
                return dct[(i, j)]
        
        return helper(0, 0)