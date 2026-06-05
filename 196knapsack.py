# Time complexity is O(2^n) and space compelxity is O(n)
class Solution:
    def knapsack(self, W, val, wt):
        def recursion(index,target):
            if index==0:
                if wt[0]<=target:
                    return val[0]
                return 0
            pick=0
            if wt[index]<=target:
                pick=val[index]+ recursion(index-1,target-wt[index])
            not_pick=recursion(index-1,target)
            return max(pick,not_pick)
        return recursion(len(val)-1,W)

# Time complexity is O(n*W) and space compelxity is O(n)+O(n*W)
class Solution:
    def knapsack(self, W, val, wt):
        dp=[[-1 for _ in range(len(val)) ] for _ in range(W+1)]
        def recursion(index,target):
            if index==0:
                if wt[0]<=target:
                    return val[0]
                return 0
                
            if dp[target][index]!=-1:
                return dp[target][index]
            pick=0
            
            if wt[index]<=target:
                pick=val[index]+ recursion(index-1,target-wt[index])
            not_pick=recursion(index-1,target)
            dp[target][index]= max(pick,not_pick)
            return dp[target][index]
        return recursion(len(val)-1,W)


# Time complexity is O(n*W) and space compelxity is O(n*W)
class Solution:
    def knapsack(self, W, val, wt):
        dp=[[0 for _ in range(len(val)) ] for _ in range(W+1)]
        for i in range(W+1):
            if i>=wt[0]:
                dp[i][0]=val[0]
        
        
        for tg in range(1,W+1):
            for index in range(1,len(val)):
                    
                pick=0
                if wt[index]<=tg:
                        
                    pick=val[index]+ dp[tg-wt[index]][index-1]
                not_pick=dp[tg][index-1]
                dp[tg][index]= max(pick,not_pick)
    
        return dp[W][len(val)-1]


# Time complexity is O(n*W) and space compelxity is O(W)
class Solution:
    def knapsack(self, W, val, wt):
        prev=[0 for _ in range(W+1)]

        for w in range(wt[0],W+1):
            prev[w]=val[0]
        
        
        for index in range(1,len(val)):

            curr=[0 for _ in range(W+1)]
            for cap in range(W+1):
                    
                pick=0
                if wt[index]<=cap:
                        
                    pick=val[index]+ prev[cap-wt[index]]
                not_pick=prev[cap]

                curr[cap]= max(pick,not_pick)
            prev=curr
    
        return prev[W]

# little space optimization to 1d array 
class Solution:
    def knapsack(self, W, val, wt):
        curr=[0 for _ in range(W+1)]

        for w in range(wt[0],W+1):
            curr[w]=val[0]
        
        
        for index in range(1,len(val)):

            for cap in range(W,wt[index]-1,-1):
                    
                pick=0
                if wt[index]<=cap:
                        
                    pick=val[index]+ curr[cap-wt[index]]
                not_pick=curr[cap]

                curr[cap]= max(pick,not_pick)
            
    
        return curr[W]