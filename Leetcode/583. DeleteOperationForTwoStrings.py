# Method 1: Memoization

# Initialize two pointers, i and j, one for each string.

# Since you do not know deleting word1[i] is better or word2[j] is better, 

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

# Method 2: DP Tabulation

# First we buid a map which width: len(word1)+1 , height : len(word2)+1, where index zero col and row means empty string

# Now we consider one thing: How many delete operation we need to match the empty string to the compared string?
# Answer will be the length of string!

# so we fill in the value into the map in the first two forloop.
# now the map look like: (take the "sea" "eat" as example)
#     " " "e" "a" "t"
# " " [0, 1, 2, 3],
# "s" [1, 0, 0, 0],
# "e" [2, 0, 0, 0],
# "a" [3, 0, 0, 0]

# then we deal with the other value:
# there are two possibility:
# (1) the next char is not same::(like the map[1][1])
# then how to match "s" and "e": we can do delete in "s" and do delete in "e" but we want to reduce the operation,
# we already have the number of oprerations for " " to match "e" , we can just add 1 deletion to make "s" become " ".
# we already have the number of oprerations for "s " to match "" , we can just add 1 deletion to make "e" become " ".
# so we can generalize the formula:

# DP[i][j] = min(DP[i][j-1]+1, DP[i-1][j]+1)

# now map looks like:
#     " " "e" "a" "t"
# " " [0, 1, 2, 3],
# "s" [1, 2, 0, 0],
# "e" [2, 0, 0, 0],
# "a" [3, 0, 0, 0]

# (2) the next char is same:(like the table[2][1]):
# we can just get the before result to fill in, since they are same so we don't need extra operation.

# DP[i][j] = DP[i-1][j-1]

# map looks like:
#     " " "e" "a" "t"
# " " [0, 1, 2, 3],
# "s"[1, 2, 0, 0],
# "e"[2, 1, 0, 0],
# "a"[3, 0, 0, 0]

# return the final value

# Credit to https://leetcode.com/john4026191/ 
# Refer from: https://leetcode.com/problems/delete-operation-for-two-strings/discuss/2149117/Python-Solution-or-DP-or-O(n*m)
class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        DP = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        
        for i in range(1,len(word2)+1):
            DP[0][i]=i
        for j in range(1,len(word1)+1):
            DP[j][0]= j
        
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]== word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i][j-1]+1, DP[i-1][j]+1)
        # print(DP)
        return DP[i][j]