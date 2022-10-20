class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        
        
        graph = [[] for i in range(numCourses)]
        
        
        for child, parent in prereq:
            graph[parent].append(child)
            
        print(graph)
        
        # check for loops
        # False if loops
        # True otherwise
        
        # 0 -> not visited
        # 1 -> visited
        # -1 -> visiting
        
        state = [0]*numCourses
        
        def hasCycle(node):
            if state[node] == 1:
                return False
            
            if state[node] == -1:
                return True # cycle
            
            state[node] = -1
            
            for child in graph[node]:
                if hasCycle(child):
                    return True
                
            state[node] = 1
            
            return False
                
        
        for node in range(numCourses):
            if hasCycle(node):
                return False
        
        return True
                
                    

            