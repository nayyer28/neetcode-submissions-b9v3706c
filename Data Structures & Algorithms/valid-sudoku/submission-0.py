class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_sets = [ set() for _ in board ]
        col_sets = [ set() for _ in board ]
        squ_sets = [ set() for _ in board ]
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                # row dup check
                if board[row][col] in row_sets[row]:
                    return False
                else:
                    row_sets[row].add(board[row][col])

                # col dup check
                if board[row][col] in col_sets[col]:
                    return False
                else:
                    col_sets[col].add(board[row][col])

                # square dup check

                squ_row = row // 3
                squ_col = col // 3

                squ_index = 3 * squ_row + squ_col


                if board[row][col] in squ_sets[squ_index]:
                    return False
                else:
                    squ_sets[squ_index].add(board[row][col])

        
        return True
                

                
