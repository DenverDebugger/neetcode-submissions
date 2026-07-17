class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # process rows - TODO: make a method
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])
        
        # process columns - TODO: make a method
        for i in range(9):
            column_set = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in column_set:
                        return False
                    else:
                        column_set.add(board[j][i])

        # process 3x3 boxes - TODO: make a method
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    curr_box = (i//3) * 3 + (j//3)
                    if board[i][j] in boxes[curr_box]:
                        return False
                    else:
                        boxes[curr_box].add(board[i][j])
        return True













