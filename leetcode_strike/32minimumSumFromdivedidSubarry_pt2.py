# TLE promblem
# class Solution(object):
#     def minimumCost(self, nums, k, dist):
#         ans=float('inf')

#         for i in range(1,len(nums)-dist):
#             temp = nums[i : i + dist + 1]

#             temp.sort()
#             curr_ans=nums[0]
#             for j in range(k-1):
#                 curr_ans=curr_ans+temp[j]
#             ans=min(ans,curr_ans)
        
#         return ans



# improved version
from bisect import bisect_left,insort

class Solution(object):
    def minimumCost(self,nums,k,dist):
        kminimum=[]  #it sotres k-1 sortest elements from the slid
        remaining=[] # it stores remaining elemnts from the slide
        i=1
        ans=0

        # build the slidning window 
        while dist-i>=0:

            # increase i along with add the values in kminimum
            insort(kminimum,(nums[i],i))
            ans+=nums[i]

            # if size of kminimum has size of k than pop extra elements also poped elements are minised and inserted into remianing for leter usage
            if len(kminimum)>k-1:
                val=kminimum.pop()
                ans-=val[0]
                insort(remaining,val)
            i+=1

        # now we build the slide now we move our slide
        result=float('inf')

        # till i reaches to last index 
        while i<len(nums):
            insort(kminimum,(nums[i],i))
            ans+=nums[i]
            if len(kminimum)>k-1:
                val=kminimum.pop()
                ans-=val[0]
                insort(remaining,val)
            
            # we got new result for next slid compare with previous slide answer 
            result=min(result,ans)

            # while we move our slide the extra elements are we have to delete 
            remove=(nums[i-dist],i-dist)

            # take position from kminimum which element we have to remove which is passed when we move the slide it give inboud answer if exites else out of bound answer
            pos=bisect_left(kminimum,remove)
            
            # if elements is in kminimum than we have to pop it and minus the sum 
            if pos < len(kminimum) and kminimum[pos]==remove:
                kminimum.pop(pos)
                ans-=remove[0]


                # than we have to take existing extra remaing elemtns from the remaining 
                if remaining:
                    smallest=remaining.pop(0)
                    insort(kminimum,smallest)
                    ans+=smallest[0]
            
            # if passed sum is in remaingn part 
            else:
                pos=bisect_left(remaining,remove)
                if pos<len(remaining) and remaining[pos]==remove:
                    remaining.pop(pos)
            i+=1
        return nums[0]+result


  
print(Solution().minimumCost([1,3,2,6,4,2,1],3,3))
        