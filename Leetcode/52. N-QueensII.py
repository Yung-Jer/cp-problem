## Since we do not need to return all distinct states (solution of where the queens are placed)
## We just have to take note of row, column, diagonals and antidiagonals
## The solution is similar to N-Queens

class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def helper(row, col_set = set(), diag_set = set(), antidiag_set = set()):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                diag = row - col
                antidiag = row + col
                
                if not (col in col_set or diag in diag_set or antidiag in antidiag_set):
                    new_col_set =  col_set.copy()
                    new_col_set.add(col)
                        
                    new_diag_set = diag_set.copy()
                    new_diag_set.add(diag)
                        
                    new_antidiag_set = antidiag_set.copy()
                    new_antidiag_set.add(antidiag)
                        
                    count += helper(row+1, new_col_set, new_diag_set, new_antidiag_set)
            return count
                    
        return helper(0)