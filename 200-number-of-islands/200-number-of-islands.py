class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def print_grid():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        print('L',end = '')
                    elif grid[i][j] == '0':
                        print('S',end = '')
                    else:
                        print(grid[i][j],end = '')
                print()

        def sink_island(i, j):
            if i < 0 or j < 0: return 
            if i >= len(grid) or j >= len(grid[0]): return
            if grid[i][j] == '0': return
            
            grid[i][j] = '0'
            
            for ai, aj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                sink_island(ai, aj)
            
        curr_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    curr_island += 1
                    sink_island(i, j)
                    #print_grid()
                    #print('---')
                
        return curr_island 
        