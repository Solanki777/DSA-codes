# time limit exceed 
class Solution:    
    def minPlatform(self, arr, dep):
        max_platform = 0
        
        # check for every train's arrival time
        for time in arr:
            count = 0
            
            for i in range(len(arr)):
                if arr[i] <= time <= dep[i]:
                    count += 1
            
            max_platform = max(max_platform, count)
        
        return max_platform
    
# optimal solution   
class Solution:
    def minPlatform(self,arr,dep):
        arr.sort()
        dep.sort()

        i=0
        j=0
        max_platfrom=0
        pt=0

        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                pt+=1
                i+=1
                max_platfrom=max(max_platfrom,pt)
            else:
                pt-=1
                j+=1
        return max_platfrom
