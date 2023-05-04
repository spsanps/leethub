# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        
        stop_h = 1000

       
        
        def rsum(node):
                      
            if node is None:
                return 0
            
            s = 0
            
            if node.val < low:
                s += rsum(node.right)
            elif node.val > high:
                s += rsum(node.left)
            else:
                s += node.val
                s += rsum(node.right)
                s += rsum(node.left)
                
            return s
    
        return rsum(root)
                
                

                
            
            
            
            
                    
        return s
                    
        