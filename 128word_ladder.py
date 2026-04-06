from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset = set(wordList)
        
        if endWord not in wordset:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    
                    new_word = word[:i] + c + word[i+1:]
                    
                    if new_word == endWord:
                        return steps + 1
                    
                    if new_word in wordset:
                        queue.append((new_word, steps + 1))
                        wordset.remove(new_word)
        
        return 0