# time complexity is O(n^2) but space complexity for all elements is O(n^2) for string length it multimply if we suppose the string length is average n/2 then the space complexity will be O(n^3)

def countDistinctSubstrings(s):
    a=set()
    
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            a.add(s[i:j])
    return len(a)+1

# optimized space complexity 
class TrieNode:
    def __init__(self):
        self.child={}
           


def countDistinctSubstrings(s):
    root=TrieNode()
    count=0

    
    for i in range(len(s)):
        node=root
        for j in range(i+1,len(s)+1):
            char=s[i:j]
            
            if char not in node.child:
                count+=1
                node.child[char]=TrieNode()
            node=node.child[char]            

    return count+1
            