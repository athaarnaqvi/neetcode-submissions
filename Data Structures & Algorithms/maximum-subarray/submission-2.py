class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minsum = nums[0]
        maxsum = nums[0]
        ans = nums[0]
        
        for i in nums[1:]:
            
            preMax = maxsum    
            maxsum = max(i,i+preMax)
            ans = max(maxsum,ans)

        return ans
