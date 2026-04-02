

class Pre: 
    def __init__ (self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.ret = Pre ()
        
    def insert(self, word: str) -> None:
        copy = self.ret
        for char in word: 
            if char not in copy.children: 
                copy.children [char] = Pre()
            copy = copy.children [char]

        copy.isEnd = True

    def search(self, word: str) -> bool:
        copy = self.ret
        for char in word: 
            if char not in copy.children: 
                return False
            copy = copy.children [char]

        return copy.isEnd
            
    def startsWith(self, prefix: str) -> bool:
        copy = self.ret
        for char in prefix: 
            if char not in copy.children: 
                return False
            copy = copy.children [char]

        return True
      