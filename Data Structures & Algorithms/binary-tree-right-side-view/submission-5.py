# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None: 
            return []

        if root.left is None and root.right is None: 
            return [root.val]

        nodes = deque ([root])

        ret = []

        while nodes: 
            leng = len (nodes)

            #for each node add the chidlren 
            for i in range (leng):
                value = nodes.popleft()
                if value.left: 
                    nodes.append (value.left)
                if value.right:
                    nodes.append (value.right)

            ret.append (value.val)

        return ret


            


        