class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        pacific= [[False] *c for _ in range(r)]
        atlantic = [[False] *c for _ in range(r)]
        result = []

        def dfs(heights, i, j,prev, group):
            if i < 0 or i >= r or j < 0 or j >= c:
                return
            if heights[i][j] < prev or group[i][j] == True:
                return
            
            group[i][j] = True
            prev = heights[i][j]
            dfs(heights,i+1,j,prev,group)
            dfs(heights,i-1,j,prev,group)
            dfs(heights,i,j+1,prev,group)
            dfs(heights,i,j-1,prev,group)


        prev = 0
        
        for i in range(r):
            dfs(heights, i, 0, 0, pacific)       # left edge
            dfs(heights, i, c - 1, 0, atlantic)  # right edge

        for j in range(c):
            dfs(heights, 0, j, 0, pacific)       # top edge
            dfs(heights, r - 1, j, 0, atlantic)  # bottom edge

        for i in range(r):
            for j in range(c):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
        return result