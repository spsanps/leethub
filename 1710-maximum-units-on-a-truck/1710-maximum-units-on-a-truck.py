class Solution(object):
    def maximumUnits(self, bT, S):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        bT.sort(key = lambda x: x[1], reverse = True)
        c = 0
        ret = 0
        #print(bT)
        for i in xrange(len(bT)):
            n, u = bT[i]
            if c + n >= S:
                #c += S - c
                ret += (S - c)*u
                break
            else:
                c += n
                ret += u*n
            #print(n, u, c, ret)
        return ret
        