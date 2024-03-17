class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        [start, end] = [newInterval[0], newInterval[1]]
        
        i=0
        n = len(intervals)
        
        # FIRST SEGMENT: pass until at insertion index
        while i<n and intervals[i][1] < start:
            result.append(intervals[i])
            i+=1
            
        # MERGE SEGMENT: merge overlapping intervals
        # note: start <= intervals[i][1]:
        while i<n and intervals[i][0] <= end:
            newInterval = [(min(newInterval[0], intervals[i][0])), max(newInterval[1], intervals[i][1])]
            i+=1
            print(newInterval)
        result.append(newInterval)
        
        # LAST SEGMENT: pass until end
        while i<n:
            result.append(intervals[i])
            i+=1
        
        return result