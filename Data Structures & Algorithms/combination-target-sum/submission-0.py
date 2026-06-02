class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, total, current):
            if total == target:
                result.append(current[:])
                return

            if i >= len(nums) or total > target:
                return

            # include nums[i]
            current.append(nums[i])
            dfs(i, total + nums[i], current)

            # backtrack
            current.pop()

            # exclude nums[i]
            dfs(i + 1, total, current)
        
        dfs(0,0,[])
        return result
        
            