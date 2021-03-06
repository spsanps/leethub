class Solution:
    def insert(self, Is: List[List[int]], nI: List[int]) -> List[List[int]]:
        
        
        if len(Is) == 0: return [nI]
        
        i = 0
        l = 0
        r = len(Is)
        
        na, nb = nI
        
        while True:
            prev_mid = i
            i = (l + r)//2
            if i == prev_mid: 
                break
                #print(l, r, mid)
            elif Is[i][0] > na:
                r = i + 1
            elif Is[i][0] < na:
                l = i - 1
            else:
                break
                
            
        
        
        #i = mid
        
        
        while i < len(Is) and Is[i][0] < na :
            i += 1
        
        if i > 0 and Is[i - 1][0] > na:
            i -= 1
        #print(i)
        
        if i == len(Is):
            Is.append(nI)
        else:
            Is.insert(i, nI)
            
        print(Is)
        
        if i > 0 and Is[i - 1][1] >= na:
            Is[i][0] = Is[i - 1][0]
            Is[i][1] = max(Is[i][1], Is[i - 1][1])
            Is.pop(i - 1)
            i -= 1
        
        i += 1
        while i < len(Is):
            if Is[i][0] <= Is[i - 1][1]:
                Is[i - 1][1] = max(Is[i][1], Is[i - 1][1])
                Is.pop(i)
            else:
                break
            
        
        return Is
            
        
        
        