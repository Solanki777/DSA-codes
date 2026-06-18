# time complexity is O(n^2) but space complexity for all elements is O(n^2) for string length it multimply if we suppose the string length is average n/2 then the space complexity will be O(n^3)

def countDistinctSubstrings(s):
    a=set()
    
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            a.add(s[i:j])
    return len(a)+1