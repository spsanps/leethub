class Solution:
    def scheduleCourse(self, c: List[List[int]]) -> int:
        q = [0]

        c.sort(key = lambda x: x[1])
        
        ct = 0
        for d, a in c:
            if ct + d <= a:
                ct += d
                heapq.heappush(q, -1*d)
            elif d > q[0]:
                ct += heapq.heappushpop(q, -1*d) + d 
            #print(q)

        return len(q) - 1