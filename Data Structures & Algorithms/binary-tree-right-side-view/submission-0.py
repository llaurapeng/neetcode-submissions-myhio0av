# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret =[]
        q = deque ([root])

        while q: 
            rightside = None

            lenQ = len (q)

            for i in range (lenQ):
                node = q.popleft()
                if node: 
                    rightside = node.val
                    rightchild = node.right
                    leftchild = node.left

                    q.append (leftchild)
                    q.append (rightchild)

            if rightside is not None: 
                ret.append (rightside)

        return ret
                    