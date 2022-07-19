class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if n == 1:
            return [[1]]
        arr = [[1], [1, 1]]
            
    
        for i in xrange(2, n):
            arr.append([1] + [arr[i - 1][k - 1] + arr[i - 1][k] for k in xrange(1, len(arr[i - 1]))] + [1])
            
        return arr
            
            
        
        
        