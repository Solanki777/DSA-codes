# A Trie (pronounced "try") is a tree-like data structure used to efficiently store and search strings, especially when many strings share common prefixes.



class Trienode:
    def __init__(self):
        self.child={}
        self.is_end=False

class Solution:
    def __init__(self):
        self.root=Trienode()

# time complexity and space complexity is O(n) 
    def insert(self,s):
        node=self.root
        for char in s:
            if char not in node.child:
                node.child[char]=Trienode()
            node=node.child[char]
        node.is_end=True

# time complexity is O(l) and space complexity is O(1)
    def search(self,word):
        node=self.root
        for char in word:
            if char not in node.child:
                return False
            node=node.child[char]
        return node.is_end


# time complexity is O(l) and space complexity is O(1)
    def starwith(self,prefix):
        node=self.root
        for char in prefix:
            if char not in node.child:
                return False
            node=node.child[char]
        return True

# Creating object
trie = Solution()

# Insert words
trie.insert("apple")
trie.insert("app")
trie.insert("bat")

# Search words
print(trie.search("apple"))   # True
print(trie.search("app"))     # True
print(trie.search("ap"))      # False

# Check prefixes
print(trie.startwith("ap"))   # True
print(trie.startwith("bat"))  # True
print(trie.startwith("cat"))  # False