#User function Template for python3
from typing import List
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        item=[]
        for i in range(len(start)):
            item.append((start[i],end[i]))
        
        item.sort(key=lamda x:x[1])
        
        last=items[0][1]
        mt=1
        for s,l in item:
            if s>last:
                last=l
                mt+=1
        
        return mt
                

# Time complexity is O(nlogn)
# space complexity is O(n)
        
        
        