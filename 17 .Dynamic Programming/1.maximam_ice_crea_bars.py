# brute force solution time complexity is O(nlogn) and space complexity is O(n) which max solution for this 
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if coins<cost:
                break
            count+=1
            coins-=cost
        return count

# recursion solution : time complexity is O(2^n) and space complexity is O(n)
class Solution:
    def recurison(self,costs,index,coins):
        if index==len(costs):
            return 0
        
        buy=0
        if coins>=costs[index]:
            buy=1+self.recurison(costs,index+1,coins-costs[index])
        not_buy=self.recurison(costs,index+1,coins)

        return max(buy,not_buy)        

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return self.recurison(costs,0,coins)
    
# recursion +dp time complexity is O(coins*len(costs)) and space complexity is O(len(costs))
class Solution:
    def recurison(self,costs,index,coins,dp):
        if index==len(costs):
            return 0
        
        if dp[index][coins]!=-1:
            return dp[index][coins]
        
        buy=0
        if coins>=costs[index]:
            buy=1+self.recurison(costs,index+1,coins-costs[index],dp)
        not_buy=self.recurison(costs,index+1,coins,dp)

        dp[index][coins]=max(buy,not_buy)

        return dp[index][coins]


    def maxIceCream(self, costs: List[int], coins: int) -> int:
        dp=[[-1 for _ in range(coins+1)] for _ in range(len(costs))]
        return self.recurison(costs,0,coins,dp)

# tabulation : time and space complexity is O(coins*len(costs))
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        dp=[[0 for _ in range(coins+1)] for _ in range(len(costs))]

        for coin in range(coins+1):
            if coin>=costs[0]:
                dp[0][coin]=1
        
        for index in range(1,len(costs)):
            for coin in range(1,coins+1):

                buy=0
                if coin>=costs[index]:
                    buy=1+dp[index-1][coin-costs[index]]
                not_buy=dp[index-1][coin]
                dp[index][coin]=max(buy,not_buy)

        return dp[len(costs)-1][coins]

# space optimization
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        prev=[0 for _ in range(coins+1)] 

        for coin in range(coins+1):
            if coin>=costs[0]:
                prev[coin]=1
        
        for index in range(1,len(costs)):
            curr=[0 for _ in range(coins+1)]
            for coin in range(1,coins+1):

                buy=0
                if coin>=costs[index]:
                    buy=1+prev[coin-costs[index]]
                not_buy=prev[coin]
                curr[coin]=max(buy,not_buy)
            prev=curr

        return prev[coins]
    
# further space optimization
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        curr=[0 for _ in range(coins+1)] 

        for coin in range(coins+1):
            if coin>=costs[0]:
                curr[coin]=1
        
        for index in range(1,len(costs)):
            for coin in range(coins,-1,-1):

                buy=0
                if coin>=costs[index]:
                    buy=1+curr[coin-costs[index]]
                not_buy=curr[coin]
                curr[coin]=max(buy,not_buy)

        return curr[coins]

        

        

        