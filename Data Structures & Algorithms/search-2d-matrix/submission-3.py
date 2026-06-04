class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])


        top, bottom = 0, ROWS - 1
        # row loop
        while top <= bottom:
            r_mid = (top + bottom) // 2

            if matrix[r_mid][0] == target:
                return True
            elif matrix[r_mid][0] > target:
                bottom = r_mid - 1
            elif matrix[r_mid][COLS-1] < target:
                top = r_mid + 1
            else:
                break
        
        # col loop
        left, right = 0, COLS - 1

        while left <= right:
            c_mid = (left + right) // 2

            if matrix[r_mid][c_mid] == target:
                return True
            elif matrix[r_mid][c_mid] > target:
                right = c_mid - 1
            else:
                left = c_mid + 1
        
        return False

