class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key = lambda x : x[1])
      
        cnt = 0
        end = float('-inf')
        for s, e in intervals:
            
            if s >= end:
                end = e
            else:
                cnt += 1
                
        return cnt
                
            
            
            
            