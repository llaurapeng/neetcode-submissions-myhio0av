# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        nodes = deque ([root])

        while nodes: 
            level = []
            leng = len (nodes)

            for i in range (leng):
                node = nodes.popleft()

                if node: 
                    level.append (node.val)
                    nodes.append (node.left)
                    nodes.append (node.right)

            if level: 
                ret.append (level)

        return ret





            
            