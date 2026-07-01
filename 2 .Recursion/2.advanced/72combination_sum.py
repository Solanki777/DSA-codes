class Solution(object):

    def recursion(self,total,index,candidates,target,result,curr_sum_set):
        
        # if target reaches to end or sum is greater than target just return 
        if total > target or index>=len(candidates):
            return
        
        # if got the curr_sum than add it into the set 
        if total==target:
            result.add(tuple(curr_sum_set.copy()))
            return 
        
        curr_sum_set.append(candidates[index])
        self.recursion(total+candidates[index],index,candidates,target ,result,curr_sum_set)
        curr_sum_set.pop()
        
        self.recursion(total,index+1,candidates,target,result,curr_sum_set)

        return result


    def combinationSum(self,candidates,target):
        result=set()
        # candidates=[2,3,5,7]
        # target=7
        self.recursion(0,0,candidates,target,result,[])
        return [list(x) for x in result]
        