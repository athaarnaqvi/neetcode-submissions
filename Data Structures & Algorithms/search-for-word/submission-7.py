class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def findword(board, i, j, w_index):
            r = len(board)
            c = len(board[0])

            if w_index == len(word):
                return True

            if i < 0 or j < 0 or i >= r or j >= c:
                return False

            if board[i][j] != word[w_index]:
                return False

            temp = board[i][j]
            board[i][j] = "$"

            found = (
                findword(board, i+1, j, w_index+1) or
                findword(board, i-1, j, w_index+1) or
                findword(board, i, j+1, w_index+1) or
                findword(board, i, j-1, w_index+1)
            )

            board[i][j] = temp
            return found

        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if findword(board, i, j, 0):
                    return True

        return False