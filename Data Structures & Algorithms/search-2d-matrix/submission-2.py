class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            midr = (top + bottom) // 2
            if target >= matrix[midr][0] and target <= matrix[midr][-1]:
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