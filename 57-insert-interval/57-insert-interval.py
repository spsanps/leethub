class Solution:
    def insert(self, Is: List[List[int]], nI: List[int]) -> List[List[int]]:
        
        
        if len(Is) == 0: return [nI]
        def bs(A, l, r):
            mid = 0
            while True:
                prev_mid = mid
                mid = (l + r)//2
                if mid == prev_mid: return mid
                #print(l, r, mid)
                if Is[mid][0] == A:
                    return mid
                elif Is[mid][0] > A:
                    r = mid + 1
                else:
                    l = mid - 1
                
            return mid
        
        na, nb = nI
        
        i = bs(na, 0, len(Is) - 1)
        
        
        while i < len(Is) and Is[i][0] < na :
            i += 1
        while i > 0 and Is[i - 1][0] > na:
            i -= 1
        #print(i)
        
        if i == len(Is):
            Is.append(nI)
        else:
            Is.insert(i, nI)
        
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
            
        
        
        