class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d={}
        
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        
        ans=1

        if 1 in d:
            if d[1]%2==0:
                ans=max(ans,d[1]-1)
            else:
                ans=max(ans,d[1])
        
        for x in d:
            if x==1:
                continue

            cur=x
            length=0

            while cur in d and d[cur]>=2:
                length+=2
                cur=cur*cur
            
            if cur in d and d[cur]>=1:
                length+=1
            
            else:
                length-=1
            
            ans=max(ans,length)
        return ans

# Time and space complexity is O(n)