class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[0]*n for _ in range m]
        cache = [[-1]*n for _ in range (m)]
        def solve(i,j):
            
            if i > m-1 or i < 0  or j > n-1 or j < 0:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if i == m-1 and j == n-1:
                cache[i][j] = 1
                return cache[i][j]
            cache[i][j] = solve(i,j+1)+solve(i+1,j)
            return cache[i][j]
        

        ways = solve(0,0)
        return ways

            
            