# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None: return root
        
        stack = [root.right, root.left]
        prev = root
        while stack:
            #print([c.val for c in stack])
            c = stack.pop()
            if c is None: continue
                
            #print(c.val)
            
            stack.append(c.right)
            stack.append(c.left)
      
            prev.right = c
            prev.left = None
            prev = c
        

                       
            
        return root
            
            
        