# time complexity is O(2^n)  and space complexity is O(n)
class Solution:
    def recursion(self, k , prices, index , tra, c_buy):
        if index==len(prices):
            return 0
        
        if tra==k:
            return 0
        
        if c_buy==1:
            buy=self.recursion(k, prices, index+1 , tra ,0) -prices[index]
            not_buy=self.recursion(k, prices, index+1 , tra ,1)
            profit=max(buy, not_buy)

        else:
            sell=self.recursion(k, prices, index+1 , tra+1 ,1) + prices[index]
            not_sell=self.recursion(k, prices, index+1 , tra ,0)
            profit=max(sell, not_sell)
            
        return profit

    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.recursion(k,prices,0,0,1)

# recursion + Dep time and space complexity is O(nk)+ stack space complexity of O(n)
class Solution:
    def recursion(self, k , prices, index , tra, c_buy,dp):
        if index==len(prices):
            return 0
        
        if tra==k:
            return 0

        if dp[index][tra][c_buy]!=-1:
            return dp[index][tra][c_buy]
        
        if c_buy==1:
            buy=self.recursion(k, prices, index+1 , tra ,0,dp) -prices[index]
            not_buy=self.recursion(k, prices, index+1 , tra ,1,dp)
            profit=max(buy, not_buy)

        else:
            sell=self.recursion(k, prices, index+1 , tra+1 ,1,dp) + prices[index]
            not_sell=self.recursion(k, prices, index+1 , tra ,0,dp)
            profit=max(sell, not_sell)
        
        dp[index][tra][c_buy]=profit
        return dp[index][tra][c_buy]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1,-1] for _ in range(k)] for _ in range(n)]
        return self.recursion(k,prices,0,0,1,dp)

# tabulation time and spac complexity is O(nk)
class Solution:
   
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0,0] for _ in range(k+1)] for _ in range(n+1)]

        for index in range(n-1,-1,-1):
            for tra in range(k-1,-1,-1):
                    buy=dp[index+1][tra][0]-prices[index]
                    not_buy=dp[index+1][tra][1]
                    profit=max(buy, not_buy)
                    dp[index][tra][1]=profit

               
                    sell=dp[index+1][tra+1][1] + prices[index]
                    not_sell=dp[index+1][tra][0]
                    profit=max(sell, not_sell)
                    dp[index][tra][0]=profit
               


        return dp[0][0][1]       

# space optimization time complexity is O(nk) and space complexity is O(k)
class Solution:
   
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        ahed=[[0,0] for _ in range(k+1)] 

        for index in range(n-1,-1,-1):
            curr=[[0,0] for _ in range(k+1)]
            for tra in range(k-1,-1,-1):
                    buy=ahed[tra][0]-prices[index]
                    not_buy=ahed[tra][1]
                    profit=max(buy, not_buy)
                    curr[tra][1]=profit

               
                    sell=ahed[tra+1][1] + prices[index]
                    not_sell=ahed[tra][0]
                    profit=max(sell, not_sell)
                    curr[tra][0]=profit
            ahed=curr

        return ahed[0][1] 
 