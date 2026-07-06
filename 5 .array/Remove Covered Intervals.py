# time complexity is O(nlogn) and space complexity is O(1)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev_i,prev_j=intervals[0]
        count=1

        for i in range(1,len(intervals)):
            if intervals[i][0]>=prev_i and intervals[i][1]<=prev_j:
                continue
            else:
                count+=1
            prev_i=intervals[i][0]
            prev_j=intervals[i][1]
        return count


        