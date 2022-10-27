# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        seen_h = 0
        
        def dfs(node, curr_h):
            
           
            
            nonlocal seen_h
                       
            if node is None:
                return
            
            if curr_h > seen_h:
                res.append(node.val)
                seen_h += 1
                
            dfs(node.right, curr_h + 1)
            
            dfs(node.left, curr_h + 1)
            
           
            
        dfs(root, 1)
        
        return res
            
            
            
        