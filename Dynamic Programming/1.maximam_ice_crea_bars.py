# brute force solution time complexity is O(nlogn) and space complexity is O(n)
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

        

        