import copy
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        initial_state = [["."] * n for i in range(n)]
        ans = []
        
        def helper(row, state, col_set = set(), diag_set = set(), antidiag_set = set()):
            if row == n:
                ans.append(["".join(i) for i in state])
                return
            else:
                for col in range(n):
                    diag = row - col
                    antidiag = row + col
                    
                    if not (col in col_set or diag in diag_set or antidiag in antidiag_set):
                        new_state = copy.deepcopy(state)
                        new_state[row][col] = "Q"
                        
                        new_col_set =  col_set.copy()
                        new_col_set.add(col)
                        
                        new_diag_set = diag_set.copy()
                        new_diag_set.add(diag)
                        
                        new_antidiag_set = antidiag_set.copy()
                        new_antidiag_set.add(antidiag)
                        
                        helper(row+1, new_state, new_col_set, new_diag_set, new_antidiag_set)
        helper(0, initial_state)
        return ans