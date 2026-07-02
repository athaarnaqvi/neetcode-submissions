class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []
        intervals.sort()
        prev_s = intervals[0][0]
        prev_e = intervals[0][1]
        for s,e in intervals[1:]:
            if s <= prev_e:
                prev_e = max(prev_e,e)
            else:
                final.append([prev_s,prev_e])
                prev_s = s
                prev_e = e
        final.append([prev_s,prev_e])
        print(final)
        return final

            
