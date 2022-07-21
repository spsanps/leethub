"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None: return node
        hmaps = {}
        hmaps[node.val] = Node(node.val)
        
        def add_to_graph(head, scan):
            for c in scan.neighbors:
               
                if c.val not in hmaps:
                    hmaps[c.val] = Node(c.val)
                    head.neighbors.append(hmaps[c.val])
                    add_to_graph(head.neighbors[-1], c)
                else:
                    head.neighbors.append(hmaps[c.val])
                    
         
                
              
        add_to_graph(hmaps[node.val], node)             
                    
        return hmaps[node.val]
        