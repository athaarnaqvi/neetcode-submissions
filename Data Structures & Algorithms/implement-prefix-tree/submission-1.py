class PrefixTree:
    counter = 0
    root = None
    def __init__(self):
        self.children = [None]*26
        self.isendofword = False

    def insert(self, word: str) -> None:
        if self.counter == 0:
            node = PrefixTree()
            self.root = node
            self.counter+=1

        current = self.root
        for c in word:
            index = ord(c)-ord("a")
            if current.children[index] is None:
                node = PrefixTree()
                current.children[index] = node
            current = current.children[index]
        
        current.isendofword = True



    def search(self, word: str) -> bool:

        current = self.root
        if current is None:
            return False
        for c in word:
            index = ord(c)-ord("a")
            if current.children[index] is None:
                return  False
            current = current.children[index]
        return current.isendofword
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        if current is None:
            return False
        for c in prefix:
            index = ord(c)-ord("a")
            if current.children[index] is None:
                return  False
            current = current.children[index]
        return True
        