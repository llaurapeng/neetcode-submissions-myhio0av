# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = []
        def helper (root, maxV):
            if root is None: 
                return 0 

            print (root.val)
            print (maxV)

            print ('-----')

            if root.val >= maxV: 
           
                ret.append (maxV)
                maxV = root.val

            helper (root.left, maxV)
            helper (root.right, maxV)

        helper (root, -1 * float ('inf'))

        return len (ret)


        