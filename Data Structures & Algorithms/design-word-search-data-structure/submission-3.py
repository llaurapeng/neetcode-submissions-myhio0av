


class TrieNode: 
    def __init__ (self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if char not in curr.children: 
                #create a node for this
                curr.children[char] = TrieNode()

            curr = curr.children [char]

        curr.isEnd = True

    def search(self, word: str):
        q = deque([(self.root, 0)])  # (node, index in the word)
        
        while q:
            node, index = q.popleft()
            
            if index == len(word):
                if node.isEnd:
                    return True
                continue  # If we reach the end of the word, but it's not a valid word, continue
            
            char = word[index]
            
            if char == '.':
                # Dot matches any character, so enqueue all children nodes at the next index
                for child in node.children.values():
                    q.append((child, index + 1))
            elif char in node.children:
                # Regular character, proceed to the next level with the corresponding child
                q.append((node.children[char], index + 1))
        
        return False
