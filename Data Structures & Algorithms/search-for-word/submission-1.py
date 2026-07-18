class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        used = {}
        
        def dfs(row, col, index):
            if index == len(word):
                return True

            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False

            if (row, col) in used:
                return False
            
            if board[row][col] != word[index]:
                return False
            
            used[(row, col)] = True

            down = dfs(row+1, col, index+1)
            up = dfs(row-1, col, index+1)
            right = dfs(row, col+1, index+1)
            left = dfs(row, col-1, index+1)

            del used[(row, col)]

            return down or up or left or right
        
        for i  in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False