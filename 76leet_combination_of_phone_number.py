
class Solution:
    def solve(self,key_map,digits,index,ans,result):
        if index>=len(digits):
            result.append("".join(ans))
            return
        
        for el in key_map[digits[index]]:
            ans.append(el)
            self.solve(key_map,digits,index+1,ans,result)
            ans.pop()

    def letterCombinations(self, digits):
        key_map={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        result=[]
        ans=[]
        self.solve(key_map,digits,0,ans,result)
        print(result)
Solution().letterCombinations("46")

# here we have to traverse each time into key_map where 4 is the largest string os we traver all 4 charcter and all 4 as also has choice to travers if n is the depth of recursion than time complexity will also for generating each string we have to merge than so it multiplay's n  O(4^n * n) and  space complexity is O(n)
        
    