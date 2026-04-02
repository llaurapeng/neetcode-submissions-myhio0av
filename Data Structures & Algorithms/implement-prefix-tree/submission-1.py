class PreNode: 
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.ret = PreNode ()

    def insert(self, word: str) -> None:
        copy = self.ret
        for x in word: 
            if x not in copy.children: 
                copy.children [x] = PreNode()        
            copy = copy.children [x]

        copy.isEnd = True


    def search(self, word: str) -> bool:
        copy = self.ret
        for x in word: 
            if x not in copy.children: 
                return False
            copy = copy.children [x]

        return copy.isEnd


    def startsWith(self, prefix: str) -> bool:
        copy = self.ret
        for x in prefix: 
            if x not in copy.children: 
                return False
            copy = copy.children [x]
        return True
        
        