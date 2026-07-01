class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items=[]
        ans=0

        for i in range(len(val)):
            items.append((wt[i],val[i],val[i]/wt[i]))
        
        items.sort(key=lambda x:x[2],reverse=True)

        for w,v,r in items:
            if capacity >=w:
                capacity-=w
                ans+=v
            else:
                ans+=capacity*r
                break
        return ans
       
        
val= [60, 100, 120]
wt= [10, 20, 30]
capacity=50
Solution().fractionalKnapsack(val,wt,capacity)

# time complexity is O(n log n)[sorting] 
# space complexity is O(n)