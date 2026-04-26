class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pref = [0] * len(nums)
        suffix = [0] * len(nums)

        # build prefix
        p = 1
        for i in range(len(nums)):
            pref[i] = p
            p *= nums[i]

        # build suffix
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = p
            p *= nums[i]

        # build result
        for i in range(len(nums)):
            result.append(pref[i] * suffix[i])

        return result