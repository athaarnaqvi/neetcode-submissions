class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            new = 1 << i
            if n & new:
                count+=1
        return count
