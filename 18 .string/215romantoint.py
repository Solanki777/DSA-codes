# Time compelxity is O(s) and space complexity is O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        ans,back=0,0
        for curr in s:
            if dict[curr]>back:
                ans=ans+dict[curr]-2*(back)
            else:
                ans+=dict[curr]
            back=dict[curr]
        return ans