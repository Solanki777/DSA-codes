# bruteforce solution 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size=len(s)
        change=0
        for i in range(0,size):
            p=set()
            p.add(s[i])
            temp=1
            for j in range(i+1,size):
                if s[j] in p:
                    break
                
                temp+=1
                p.add(s[j])
            change=max(temp,change)
        
        return change
    
# optimal Solution

# time complexity is O(n) space complexity O(min(n,dictionary))

class Solution:
    def lengthOfLongestSubstring(self,s):
        left=0
        right=0
        maxi=0
        dic={}
        size=len(s)
        while right<size:
            if s[right] in dic:
                left=max(left,dic[s[right]]+1)
            
            dic[s[right]]=right
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
    
                
                