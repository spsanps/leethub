class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        a = a[::-1]
        b = b[::-1]
        res = ''
        for i in range(max(len(a), len(b))):
            if i < len(a):
                if a[i] == '1':
                    ai = 1
                else:
                    ai = 0
            else:
                ai = 0
            
            if i < len(b):
                if b[i] == '1':
                    bi = 1
                else:
                    bi = 0
            else:
                bi = 0
                
            r = ai + bi + c
            
            if r == 3:
                res += '1'
                c = 1
            elif r == 2:
                res += '0'
                c = 1
            elif r == 1:
                c = 0
                res += '1'
            else:
                c = 0
                res += '0'
            
            
        if c == 1: res += '1'
            
        return res[::-1]
            
            
            
            
            