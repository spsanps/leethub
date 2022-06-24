class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
    
        target = [-1*i for i in target]
        heapq.heapify(target)
        n = len(target)

        
        def pos(t, s):
            if s == n: return True
            #if t[0] == -n: return True
            #elif -t[0] < n: return False           

            lt = -heapq.heappop(t)
            if (s - lt) == 1: x = 1
            elif (s - lt) < 1: return False
            else: x = lt%(s - lt)
            if x >= lt: return False
            s += x - lt
            #print(t, x, s, lt)
            if x != 1:
                if x < n: return False
            
          
            
            heapq.heappush(t, -x)
            return pos(t, s)

            
        return pos(target, -sum(target))