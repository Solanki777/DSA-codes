class Solution(object):
    def solve(self,candidates,target,ans,result,total,index):
        if index >= len(candidates):
            return
        if total==target:
            result.add(tuple(ans))
            return
        
        if total>target:
            return 
        
        for i in range(index,len(candidates)):
            # skip duplicates
            if i > index and candidates[i]==candidates[i-1]:
                continue
            ans.append(candidates[i])
            self.solve(candidates,target,ans,result,total+candidates[i],i+1)
            ans.pop()



    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=set()
        ans=[] 
        self.solve(candidates,target,ans,result,0,0)
        return [list(t) for t in result]


candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))

# each element has two choice chosen or not so 2 and for n elemnent it becomes 2^n we have to check for every element so it becomes 2^n*n time complexity

# for space complexity is O(N) which is you stack space and in extra we have result and list which can be negligible complaretively