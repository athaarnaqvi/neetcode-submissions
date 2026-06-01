class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                node = TrieNode()
                current.children[c] = node
        
            current = current.children[c]
        current.word = True
    
    


    def search(self, word: str) -> bool:
        def dfs(root,j):
            current = root
            if j == len(word):
                return current.word
            c = word[j]
            if c == ".":
                for child in current.children.values():
                    if dfs(child,j+1):
                        return True
                return False
            if c not in current.children:
                    return False
        
            return dfs(current.children[c],j+1)
        return dfs(self.root,0)
                
                
                    

