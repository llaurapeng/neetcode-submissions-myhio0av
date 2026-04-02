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
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root
            






