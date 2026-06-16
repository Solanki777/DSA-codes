class Trienode:
    def __init__(self):
        self.child={}
        self.c_p=0
        self.endings=0
class Trie:
    def __init__(self):
        self.root=Trienode()
        
    # Time complexity and space compelxity is O(n) 
    def insert(self, word):
        node=self.root

        for char in word:
            if char not in node.child:
                node.child[char]=Trienode()
            node=node.child[char]
            node.c_p+=1
        node.endings+=1

    # time comlplexity is O(n) and space compexity is O(1)
    def countWordsEqualTo(self, word):
        node=self.root

        for char in word:
            if char not in node.child:
                return 0
            node=node.child[char]
        return node.endings
        

    # time comlplexity is O(n) and space compexity is O(1)
    def countWordsStartingWith(self, word):
        node=self.root
        for char in word:
            if char not in node.child:
                return 0
            node=node.child[char]
        return node.c_p

    # time comlplexity is O(n) and space compexity is O(1)
    def erase(self, word):
        node=self.root
        for char in word:
            if char not in node.child:
                return
            node=node.child[char]
            node.c_p-=1
        node.endings-=1
                
       