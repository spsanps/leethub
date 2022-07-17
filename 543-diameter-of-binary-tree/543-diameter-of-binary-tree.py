# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_chain = 0
        
        def dfs_depth(self, head, h):
            
            if head is None: return h - 1
            
            l = dfs_depth(self, head.left, h + 1)
            r = dfs_depth(self, head.right, h + 1)
            
            lh = l - h
            rh = r - h
            
            if lh + rh > self.max_chain:
                self.max_chain = lh + rh
            
            return max(l, r)
        
        dfs_depth(self, root, 1)
            
        return self.max_chain
            
            
            
            