class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        i=1
        
        minprod = nums[0]
        maxprod = nums[0]
        ans = nums[0]
        while(i<len(nums)):
            premin = minprod
            premax = maxprod

            minprod = min(nums[i], nums[i] * premin, nums[i]* premax)
            maxprod = max(nums[i], nums[i] * premin, nums[i]* premax)

            ans = max(ans,maxprod)
            i+=1
        
        return ans
        

        