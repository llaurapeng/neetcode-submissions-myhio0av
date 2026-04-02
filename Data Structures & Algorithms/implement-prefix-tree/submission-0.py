

class TreeNode: 
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in list (word): 
            if char not in curr.children: 
                curr.children [char] = TreeNode()
            #if char is already in the curr children then just incrememt

            curr = curr.children [char]

        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.root

        for char in list (word): 
            if char not in curr.children: 
                return False

            curr = curr.children [char]

        if curr.isEnd == True: 
            return True

        else: 
            return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix: 
            if char not in curr.children: 
                return False

            curr = curr.children [char]

        return True
        
        