class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to keep track of seen numbers
        row_set = [set() for _ in range(9)]
        col_set = [set()for _ in range(9)]
        grid_set =[set() for _ in range(9)]
        
        for r in range(9) :
            for c in range(9):
                val = board[r][c]

                if val == '.' :
                    continue
                box_idx = (r//3) * 3 + (c//3)
            
                if val in row_set[r] or val in col_set[c] or val in grid_set[box_idx] :
                    return False
            
                if val in row_set[r] or val in col_set[c] or val in grid_set[box_idx]:
                    return False
                
            # Add the value to our tracking sets
                row_set[r].add(val)
                col_set[c].add(val)
                grid_set[box_idx].add(val)
            
        return True