class Solution(object):
    def maxArea(self, h, w, hCs, vCs):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        hCs.sort()
        vCs.sort()
        
        hCs = hCs + [h]
        vCs = vCs + [w]
        
        maxH = hCs[0]
        maxV = vCs[0]
        
        for i in xrange(1, len(hCs)):
            n = hCs[i] - hCs[i - 1]
            if (n > maxH): maxH = n
        
        for i in xrange(1, len(vCs)):
            n = vCs[i] - vCs[i - 1]
            if (n > maxV): maxV = n
        
        return (maxH*maxV)%(10**9 + 7)