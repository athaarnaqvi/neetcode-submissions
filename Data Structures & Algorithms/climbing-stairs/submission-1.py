class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache =[-1]*46
       
        def climb(n):
            if self.cache[n] != -1:
                return self.cache[n]
            if n == 0:
                return 1
            if n<0:
                return 0

            onestep=climb(n-1)
            twostep=climb(n-2)
            total = onestep+twostep
            self.cache[n] = total
            return self.cache[n]
       
        ways=climb(n)

        return ways

        