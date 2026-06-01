class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isendofword = False
        self.word = ""

    def insert(self, word: str):
        current = self
        for c in word:
            index = ord(c) - ord("a")
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.word = word
        current.isendofword = True

class Solution:
    def __init__(self):
        self.result = []

    def findTrieWord(self, board, i, j, root):
        r = len(board)
        c = len(board[0])

        if (i < 0 or i >= r or j < 0 or j >= c or
            board[i][j] == "$" or
            root.children[ord(board[i][j]) - ord("a")] is None):
            return

        root = root.children[ord(board[i][j]) - ord("a")]

        if root.isendofword:
            self.result.append(root.word)
            root.isendofword = False

        temp = board[i][j]
        board[i][j] = "$"

        self.findTrieWord(board, i+1, j, root)
        self.findTrieWord(board, i-1, j, root)
        self.findTrieWord(board, i, j+1, root)
        self.findTrieWord(board, i, j-1, root)

        board[i][j] = temp

    def findWords(self, board, words):
        trie = TrieNode()

        for w in words:
            trie.insert(w)

        self.result = []

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                idx = ord(board[i][j]) - ord("a")
                if trie.children[idx] is not None:
                    self.findTrieWord(board, i, j, trie)

        return self.result  