class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        ps = intervals[0][0]
        pe = intervals[0][1]
        number = 0
        for s,e in intervals[1:]:
            if pe <= s:
                ps = s
                pe = e
                continue
            elif pe <= e:
                number += 1 
            elif pe > e:
                ps = s
                pe = e
                number += 1

        
        return number