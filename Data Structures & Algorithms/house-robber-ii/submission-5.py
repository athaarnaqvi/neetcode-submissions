class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*101
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        def r(i,n):
            
            if (i>n):
                return 0
            if cache[i] != -1:
                return cache[i]
                
            steal = nums[i] + r(i+2,n)
            skip = r(i+1,n)

            cache[i] = max(steal,skip)
            return cache[i]
        
        stealzero = r(0,n-2)
        cache = [-1]*101
        skipzero = r(1,n-1)
        money = max(stealzero,skipzero)
        return money
        