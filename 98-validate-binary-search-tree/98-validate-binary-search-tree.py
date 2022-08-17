# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, l = None, u = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        
        if l is not None and l >= root.val:
            return False
        if u is not None and u <= root.val:
            return False
        
        return self.isValidBST(root.left, l, root.val) and self.isValidBST(root.right, root.val, u)
        