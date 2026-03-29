class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, len(matrix[0]) - 1
        top, bottom = 0, row

        while top <= bottom:
            midr = (top + bottom) // 2
            if target >= matrix[midr][0] and target <= matrix[midr][col]:
                break
            if target < matrix[midr][0]:
                bottom = midr - 1
            else:
                top = midr + 1

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            midc = (left + right) // 2

            if target == matrix[midr][midc]:
                return True
            
            if target < matrix[midr][midc]:
                right = midc - 1
            else:
                left = midc + 1

        return False 