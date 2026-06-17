
class Trienode:
    def __init__(self):
        self.child={}
        self.is_end=False

class Solution:
    def __init__(self):
        self.root=Trienode()

# for each insertion time complexity will be O(Length)
    def insert(self,s):
        node=self.root

        for word in s:
            if word not in  node.child:
                node.child[word]=Trienode()
            node=node.child[word]

        node.is_end=True
    
    # for each insertion time complexity will be O(Length)
    def check_prefix_exits(self,str):
        node=self.root
        
        for word in str:

            if word not in node.child:
                return False
            node=node.child[word]

            if not node.is_end:
                return False
        return True

    
# total time complexity is O(L) and space complexity is O(Number of disting nodes)
def completeString(n: int, a: List[str])-> str:
    sl=Solution()

    for str in a:
        sl.insert(str)

    ans=""
    
    for str in a:
        if sl.check_prefix_exits(str)==True:
            if len(str)>len(ans) or (len(str)==len(ans) and str<ans):
                ans=str
            
    if ans=="":
        return None
    return ans
    



    
   