# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        ret = []
        
        if root is None: return ret
        
        def dfs(head, level):
            if len(ret) <= level:
                ret.append([head.val])
            else:
                ret[level].append(head.val)
            if head.left is not None:
                dfs(head.left, level + 1)
            if head.right is not None:
                dfs(head.right, level + 1)
        
        dfs(root, 0)
        
        return ret
            
                
            