class Solution(object):
    def solve(self,ele,sum,total,result,ans,index):

        if len(ans)==ele and total==sum:
            result.append(ans[:])
            return
        
        if total>sum:
            return
        if index>9:
            return
        
        ans.append(index)
        self.solve(ele,sum,total+index,result,ans,index+1)
        ans.pop()
        self.solve(ele,sum,total,result,ans,index+1)

    def combinationSum3(self, k, n):
        result=[]
        self.solve(k,n,0,result,[],1)
        print(result)

print(Solution().combinationSum3(3,9))
# time complexity is O(1) because we take 7