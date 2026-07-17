class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        num_cols = len(matrix[0])
        while low <= high:
            mid = (low + high) // 2
            row = mid // num_cols
            col = mid % num_cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False