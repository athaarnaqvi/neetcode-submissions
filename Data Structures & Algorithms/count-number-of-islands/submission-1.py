class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        group = 0
        r = len(grid)
        c = len(grid[0])
        
        def dfs(grid: List[List[str]], i: int, j:int):
            r = len(grid)
            c = len(grid[0])
            if i>=r or i <0 or j>=c or j<0 or grid[i][j] == "0":
                return 
        
            grid[i][j] = "0"

            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)

            

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    group+=1
                    dfs(grid, i, j)

        return group