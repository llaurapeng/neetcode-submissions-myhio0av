# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #use bfs

        if root is None: 
            return ''
        ret = []
        q = deque ([root])

        while q: 
            leng = len (q)

            for i in range (leng):
                node = q.popleft ()
                if node is None: 
                    ret.append ('n')

                else: 
                    ret.append (str(node.val))
                    q.append (node.left)
                    q.append (node.right)

        return ' '.join (ret) 

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if len(data) == 0: 
            return None
        data = data.split (' ')
        
        ret = TreeNode ( int (data [0]))

        data = list(data[1:])
        roots = [ret]

        while data:
            node = roots.pop (0)
            #left part is not none
            if data[0] != 'n':
                left = TreeNode (int (data [0]))
                roots.append (left)
            else: 
                left = None
            #right part is not none
            if data [1] != 'n':
                right = TreeNode (int (data [1]))
                roots.append (right)
            else: 
                right = None
    
            node.left = left
            node.right = right

            data.pop (0)
            data.pop (0)

        return ret




        

