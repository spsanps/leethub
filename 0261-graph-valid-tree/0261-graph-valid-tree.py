class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        #print(graph)
        
        
        visited = [0]*n 
        
        def isValid(node, prev):
            
            prev = deque(prev)
            
            #print(node, prev)
            
            if prev.popleft() == node:
                return True
            
            prev.append(node)
            
            if visited[node] == 1: # visited
                return True
            
            if visited[node] == -1: # visiting
                return False
            
            
            # else
            visited[node] = -1
            
            r = all([isValid(c, prev) for c in graph[node]])
            
            visited[node] = 1
            
            #print("Result: ", r)
            
            return r
        
        r = isValid(0, prev = deque([None, None]))
        
        if r is False: return False
        
        for i in range(n):
            if visited[i] != 1:
                return False
        
        return True
            

            
            
            