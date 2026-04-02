# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        nodes = deque([root])
        ret = []

        while nodes: 
            rightSide = None
            leng = len (nodes)
            for i in range (leng):
                node = nodes.popleft()
                if node: 
                    rightSide = node
                    nodes.append (node.left)
                    nodes.append (node.right)
            if rightSide: 
                ret.append (rightSide.val)

        return ret




        