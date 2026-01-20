
# brute force solution
# class Solution:

#     def is_sum(self,i,j,max_size,grid,target):
#         temp=0
#         for r in range(i,i+max_size):
#             for c in range(j,j+max_size):
#                 temp+=grid[r][c]
#         if temp<=target:
#             return True
#         return False
#     def check_thre(self,grid,th):

#         m=len(grid)#rows
#         n=len(grid[0])#cols
        
#         # maximum squre size
#         max_size=min(m,n)

#         while max_size>=1:
#             for i in range(m-max_size+1):
#                 for j in range(n-max_size+1):
#                     c=self.is_sum(i,j,max_size,grid,th)
#                     if c:
#                         return max_size
#             max_size-=1
#         return 0

    
# optimal solution
# class Solution():
#     def is_check(self,i,j,max_size,th,pre_row):
#         temp=0
#         for r in range(i,i+max_size):
#             temp+=pre_row[r][j+max_size]-pre_row[r][j]
#         if temp<=th:
#             return True
#         return False
 
#     def check_thre(self,grid,th):
#         m=len(grid) #rows
#         n=len(grid[0]) #col

#         # build the row ans column prefix table 
#         pre_row=[[0]*(n+1) for _ in range(m)]

#         for i in range(0,m):
#             for j in range(0,n):
#                 pre_row[i][j+1]=grid[i][j]+pre_row[i][j]
        
#         # max size that possible from the grid
#         max_size=min(m,n)

#         while max_size>=1:
#             for i in range(m-max_size+1):
#                 for j in range(n-max_size+1):
#                     if self.is_check(i,j,max_size,th,pre_row):
#                         return max_size
#             max_size-=1
#         return 0


# optimized solution
class Solution:
    def buildpre(self,grid,th):
        m=len(grid) #row
        n=len(grid[0]) #col

        # build the prefix matrix
        pref=[[0]*(n+1)for _ in range(m+1)]
       
        # fill the prefix table
        for i in range(1,m+1):
            for j in range(1,n+1):
                pref[i][j]=pref[i-1][j]+pref[i][j-1]-pref[i-1][j-1]+grid[i-1][j-1]
        
        # check the ans
        def can(size):
            for i in range(m-size+1):
                for j in range(n-size+1):
                    total=pref[i+size][j+size]-pref[i+size][j]-pref[i][j+size]+pref[i][j]
                    if total<=th:
                        return True
            return False
        
        # binary search
        ans=0
        lo=0
        hi=min(m,n)
        while lo<=hi:
            mid=(lo+hi)//2
            if can(mid):
                ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans

    
grid=[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold_val=4
s=Solution()
print(s.buildpre(grid,threshold_val))



