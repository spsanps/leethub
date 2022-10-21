class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        # create graph
        
        graph = [[] for _ in range(numCourses)]
        for child, parent in prerequisites:
            graph[parent].append(child)
            
            
        #print(graph)
        #print(isroot)
        
        visiting = [0 for _ in range(numCourses)]
        
        
        def check_below(node):
            
            #print(node)
            #print(visiting)
            
            if visiting[node] == 1: return []
            
            if visiting[node] == -1: return -1
            
            visiting[node] = -1
            
            res = []
            
            for c in graph[node]:
                r = check_below(c)
            
                if r == -1:
                    return -1
                
                res.extend(r)
        
            
            res.append(node)
            
            visiting[node] = 1

            return res
        
        res = []

        for i in range(numCourses):
            if visiting[i] == 1: continue
                  
            r = check_below(i)
            #print(i, r)
            
            if r == -1: return []
            
            res.extend(r)
        
        return res[::-1]
            
            