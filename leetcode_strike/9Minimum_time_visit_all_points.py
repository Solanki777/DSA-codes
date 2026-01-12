class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        n=len(points)
        ans=0
        for al in range(n-1):
            (x1,y1)=points[al]
            (x2,y2)=points[al+1]
            maxi=max(abs(x2-x1),abs(y2-y1))
            ans+=maxi
        return ans


        


points=[[1,1],[3,4],[-1,0]]
sl=Solution()
print(sl.minTimeToVisitAllPoints(points))