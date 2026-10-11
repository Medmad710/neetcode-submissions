import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = bisect.bisect_left(intervals, newInterval)
        res = list(newInterval)  # Создаем копию, чтобы не мутировать оригинал
        
        for i in range(idx, len(intervals)):
            if intervals[i][0] <= res[1]:
                res[0] = min(res[0], intervals[i][0])
                res[1] = max(res[1], intervals[i][1])
                intervals[i] = 0
            else:
                break
                
        for i in range(idx - 1, -1, -1):
            if intervals[i][1] >= res[0]:
                res[0] = min(res[0], intervals[i][0])
                res[1] = max(res[1], intervals[i][1])
                intervals[i] = 0
            else:
                break
                
        intervals = [x for x in intervals if x != 0]
        bisect.insort(intervals, res)
        return intervals