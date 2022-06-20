class Solution(object):
    
    def dis(p):
        return p[0]**2 + P[1]**2
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2)[:k]
        
        