class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        s = []
        
        for t in tokens:
            
            if t in "*-+/":
                op = t
                b = int(s.pop())
                a = int(s.pop())
                if op == '*':
                    s.append(a*b)
                elif op == '+':
                    s.append(a+b)
                elif op == '-':
                    s.append(a-b)
                elif op == '/':
                    k = a//b
                    if k < 0 and a%b != 0: k += 1
                    s.append(k)
            else:
                s.append(t)
                
            #print(s)
            
        return s[0]
        
        
            