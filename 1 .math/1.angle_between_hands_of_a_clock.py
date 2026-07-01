class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minut_degree=minutes*6
        hour_degree=hour*30

        # set hour
        degree_moved=minutes*0.5
        hour_degree+=degree_moved

        ans=abs(hour_degree-minut_degree)

        if ans>180:
            return 360-ans
        return ans


# Time complexity and space complexity is O(1)
       