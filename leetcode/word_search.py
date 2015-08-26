class Solution(object):
    def board_exist(self, board, word, i, j, index, visited):
        if index == len(word):
            return True
        rows,cols = len(board), len(board[0])
        if i == rows or i < 0 or j == cols or j < 0 or word[index] != board[i][j] or visited.get((i,j)):
            return False
        visited[(i,j)] = True
        ret = self.board_exist(board, word, i + 1, j, index + 1, visited) \
               or self.board_exist(board, word, i - 1, j, index + 1, visited) \
               or self.board_exist(board, word, i, j + 1, index + 1, visited) \
               or self.board_exist(board, word, i, j - 1, index + 1, visited)
        visited[(i,j)] = False
        return ret
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,cols = len(board), len(board[0])
        index = 0
        visited = {}
        for i in range(0, rows):
            for j in range(0, cols):
                if self.board_exist(board, word, i, j, index, visited):
                    return True
        return False