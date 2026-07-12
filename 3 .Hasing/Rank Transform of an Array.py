# time complexity is O(nlogn) and space complexity is O(n)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = arr.copy()
        temp.sort()
        index={}
        ans=[]
        renk=1

        for el in temp:
            if el not in index:
                index[el]=renk
                renk+=1
        
        for el in arr:
            ans.append(index[el])

        return ans
