# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []
        q = deque ([root])

        while q: 
            qlen = len (q)
            #for every node add it's children into the queue
            for i in range (qlen): 
                node = q.popleft()
                if node: 
                    ret.append (str (node.val))
                else: 
                    ret.append ('N')

               
                if node: 
                    q.append (node.left)  
                    q.append (node.right)

        return ",".join (ret)
        

        
    # Decodes your encoded data to tree.

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        ret = TreeNode(int(vals[0]))
        q = deque([ret])
        index = 1

        while q: 
            root = q.popleft()

            if vals[index] != 'N':
                leftNode = TreeNode (int (vals[index]))
                root.left = leftNode
                q.append (leftNode)

          
            index+=1

            if vals[index] != 'N':
                rightNode = TreeNode (int (vals [index]))
                root.right = rightNode
                q.append (rightNode)


            index+=1

        return ret



