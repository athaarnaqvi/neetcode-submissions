class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices ={}
        for n in range(len(nums)):
            if target-nums[n] in indices:
                return [indices[target-nums[n]],n]
            
            indices[nums[n]]=n


