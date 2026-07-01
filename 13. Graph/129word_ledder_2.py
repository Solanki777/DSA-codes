from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordset = set(wordList)
        if endWord not in wordset:
            return []
        
        queue = deque()
        queue.append([beginWord])   # store path
        
        result = []
        found = False
        
        while queue and not found:
            level_visited = set()
            
            for _ in range(len(queue)):
                path = queue.popleft()
                word = path[-1]
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word == endWord:
                            result.append(path + [new_word])
                            found = True
                        
                        if new_word in wordset:
                            queue.append(path + [new_word])
                            level_visited.add(new_word)
            
            # remove after level ends
            wordset -= level_visited
        
        return result
# Leetcode TLE due to last checking and takes time for slicing but same method in c++ dones easily
# Time complexity is O(26*l*n*k)=O(l*n^2) and space complexity isO (N^2)
        