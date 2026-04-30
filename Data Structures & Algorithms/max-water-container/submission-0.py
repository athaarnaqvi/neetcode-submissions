class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maximum = 0
        while i < j:
            water = (j - i) * min(heights[i], heights[j])
            if (water > maximum):
                maximum = water
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return maximum