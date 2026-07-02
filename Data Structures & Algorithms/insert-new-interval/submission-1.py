class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final = []
        inserted = False   
        for s,e in intervals:
            if e < newInterval[0]:
                final.append([s,e])
                continue
            elif s > newInterval[1]:
                if not inserted:
                    final.append(newInterval)
                    inserted = True
                final.append([s, e])
            else:
                # merge
                newInterval[0] = min(newInterval[0],s)
                newInterval[1] = max(newInterval[1],e)
                
        
        if not inserted:
            final.append(newInterval)

        return final

                    
            