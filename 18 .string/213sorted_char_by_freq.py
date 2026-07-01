class Solution:
    def frequencySort(self, s: str) -> str:
        count={}
        result=""

        for char in s:
            if char not in count:
                count[char]=1
            else:
                count[char]+=1
        
        # it will return Tuple like ((e,3),(f,4))
        sorted_count=sorted(count.items(),key=lambda x:x[1] ,reverse=True)

        for i in sorted_count:
            for _ in range(i[1]):
                result+=i[0]
        return result

# time complexity is O(n)+O(nlogn)+O(n) and space compelxity is O(n)
        
        

