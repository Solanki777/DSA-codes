# pure recursion time complexity is o(3^n) and space complexity is O(n)
class Solution:
    def maximumPoints(self, mat):
        days=len(mat)-1
        lasti=len(mat[0])

        def solve(day,last):
            # base codition 
            if day==0:
                maxi=0
                for i in range(len(mat[day])):
                    
                    if i!=last:
                        maxi=max(maxi,mat[day][i])
                return maxi
            maxi=0
            for i in range(len(mat[day])):
                
                if i!=last:
                    maxi=max(maxi,mat[day][i]+solve(day-1,i))

            return maxi
        return solve(days,lasti)

# dp with recursion time complexity is O(n) and space complexity is O(4n+n)
class Solution:
    def maximumPoints(self, mat):
        days=len(mat)
        lasti=len(mat[0])
        dp=[[-1 for _ in range(lasti+1)]for _ in range(days)]

        def solve(day,last):
            # base codition 
            if day==0:
                maxi=0
                for i in range(len(mat[day])):
                    
                    if i!=last:
                        maxi=max(maxi,mat[day][i])
                return maxi
            
            if dp[day][last]!=-1:
                    return dp[day][last]
            
            maxi=0
            for i in range(len(mat[day])):

                
                
                if i!=last:
                    maxi=max(maxi,mat[day][i]+solve(day-1,i))

            dp[day][last]=maxi
            return maxi
        return solve(days-1,lasti)

# tabulation here dp size complexity is days*task and time complexity is O(n) for 3 days and 3 task it is 9n
class Solution:
    def maximumPoints(self, mat):
        days = len(mat)
        tasks= len(mat[0])
        
        # maximum points till this day
        dp=[[0 for _ in range (tasks)] for _ in range(days)]

        # on first day we do not do any task previously so the answer is current task 
        for i in range(tasks):
            dp[0][i]=mat[0][i]
        
        for day in range(1,days):
            for task in range(tasks):
                maxi=0
                for prev in range(tasks):
                    if prev!=task:
                        maxi=max(maxi,dp[day-1][prev])
                dp[day][task]=mat[day][task]+maxi
        return max(dp[days-1])

# optimal time complexity is O(n) and space complexity is O(1)
class Solution:
    def maximumPoints(self, mat):
        days = len(mat)
        tasks= len(mat[0])
        
        # maximum points till this day
        prev=[0 for _ in range (tasks)]

        # on first day we do not do any task previously so the answer is current task 
        for i in range(tasks):
            prev[i]=mat[0][i]
        
        for day in range(1,days):
            curr=[0]*tasks
            for task in range(tasks):
                maxi=0
                for prev_task in range(tasks):
                    if prev_task!=task:
                        maxi=max(maxi,prev[prev_task])
                curr[task]=mat[day][task]+maxi
            prev=curr
        return max(prev)
