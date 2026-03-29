class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = len(board)
        # track row uniqueness
        row_sets = [set() for _ in range(SIZE)]
        print(row_sets)
        # track col uniqueness
        col_sets = [set() for _ in range(SIZE)]
        # track square uniquenes
        box_sets = [set() for _ in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                # ignore empty
                if board[i][j] == ".":
                    continue
                # row uniqueness check
                if board[i][j] in row_sets[i]:
                    return False
                else:
                    row_sets[i].add(board[i][j])
                
                # col uniqueness check
                if board[i][j] in col_sets[j]:
                    return False
                else:
                    col_sets[j].add(board[i][j])
                
                # box uniqueness check
                if board[i][j] in box_sets[3 * (i//3) + j//3]:
                    return False
                else:
                    box_sets[3 * (i//3) + j//3].add(board[i][j])
        return True
