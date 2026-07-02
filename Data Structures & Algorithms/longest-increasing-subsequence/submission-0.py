class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [[-1]*1001 for _ in range(1001)]
        
        def solve(i, prev):
            if i >= len(nums):
                cache[i] = 0
                return cache[i]
            if cache[i][prev] != -1:
                return cache[i][prev]
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(i+1,i)
            skip = solve(i+1,prev)

            cache[i][prev] =  max(take,skip)
            return cache[i][prev]

        
        length = solve(0,-1)
        return length
                     