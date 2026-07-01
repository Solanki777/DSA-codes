class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic={'a':0,'b':0,'c':0}

        left=0
        right=0
        count=0

        while right <len(s):
            dic[s[right]]+=1

            while dic['a']>0 and dic['b']>0 and dic['c']>0 :
                dic[s[left]]-=1
                left+=1
                count+=len(s)-right
            right+=1

        return count

# Time complexity is O(n) and space compelxity is O(1)