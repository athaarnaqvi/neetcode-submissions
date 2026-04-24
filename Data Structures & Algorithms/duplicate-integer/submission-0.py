class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set();
        for l in nums:
            if (l in s):
                return True
            else:
                s.add(l)
        return False
        