class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        minimum = 1001
        start = 0
        end = len(nums)

        while start < end:
            if nums[end//2] < minimum:
                minimum = nums[end//2]
                end = end//2
            else:
                start = nums[end//2]
        return minimum