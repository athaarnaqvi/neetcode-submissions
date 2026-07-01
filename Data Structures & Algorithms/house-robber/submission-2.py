class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*101
        def r(i):
            
            if (i>=len(nums)):
                return 0
            if cache[i] != -1:
                return cache[i]
                
            steal = nums[i] + r(i+2)
            skip = r(i+1)

            cache[i] = max(steal,skip)
            return cache[i]
        
        money = r(0)

        return money
        


            
