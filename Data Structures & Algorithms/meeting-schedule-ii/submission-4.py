"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        
        maxoverlaps = 0
        overlaps = 0
        for i in intervals:
            events.append([i.start,+1])
            events.append([i.end,-1])
        # events.sort(key=lambda interval: interval.start)
        events.sort()

        for e,r in events:
            overlaps += r
            maxoverlaps = max(overlaps,maxoverlaps)


        
        return maxoverlaps