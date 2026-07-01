
# pure_recursion  time complexity is O(n^2) and space complexity is O(n)
class Solution:
    def recursion(self,index,can_b,prices):
        if index==len(prices):
            return 0
        
        if can_b==1:
            buy=-prices[index]+self.recursion(index+1,0,prices)
            not_buy=self.recursion(index+1,1,prices)
            profit=max(buy,not_buy)

        else:
            sell=prices[index]+self.recursion(index+1,1,prices)
            not_sell=self.recursion(index+1,0,prices)
            profit=max(sell,not_sell)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.recursion(0,1,prices)
        

# pure_recursion +dp time complexity is O(n*2) and space complexity is O(n) + dp(n*2)
class Solution:
    def recursion(self,index,can_b,prices,dp):
        if index==len(prices):
            return 0
        
        if dp[index][can_b]!=-1:
            return dp[index][can_b]
        
        if can_b==1:
            buy=-prices[index]+self.recursion(index+1,0,prices,dp)
            not_buy=self.recursion(index+1,1,prices,dp)
            profit=max(buy,not_buy)

        else:
            sell=prices[index]+self.recursion(index+1,1,prices,dp)
            not_sell=self.recursion(index+1,0,prices,dp)
            profit=max(sell,not_sell)
        dp[index][can_b]= profit
        return dp[index][can_b]

    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1,-1] for _ in range(len(prices))]
        return self.recursion(0,1,prices,dp)
    

# tabulation time complexity is O(n) and space complexity is O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0,0] for _ in range(n+1)]
        

        for index in range(len(prices)-1,-1,-1):

            buy=-prices[index]+dp[index+1][0]
            not_buy=dp[index+1][1]
            dp[index][1]=max(buy,not_buy)
            
            sell=prices[index]+dp[index+1][1]
            not_sell=dp[index+1][0]
            dp[index][0]=max(sell,not_sell)

        return dp[0][1]

# space optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prev=[0,0]
        

        for index in range(len(prices)-1,-1,-1):
            curr=[0,0]

            buy=-prices[index]+prev[0]
            not_buy=prev[1]
            curr[1]=max(buy,not_buy)
            
            sell=prices[index]+prev[1]
            not_sell=prev[0]
            curr[0]=max(sell,not_sell)

            prev=curr

        return prev[1]

        
