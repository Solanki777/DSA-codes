class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0, 20: 0}
        ans=True

        for item in bills:
            if item==5:
                d[5]+=1
            elif item==10:
                d[10]+=1
                if d[5]>=1:
                    d[5]-=1
                else:
                    return False
            else:
                d[20]+=1
                if d[10]>=1 and d[5]>=1:
                    d[10]-=1
                    d[5]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
        return True
        
# time complexity is O(n) and space complexity is O(1)