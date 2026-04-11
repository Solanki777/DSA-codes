from collections import defaultdict, deque

class Solution:
    def findOrder(self, words):
        adjlist = defaultdict(list)
        indegree = defaultdict(int)
        tword=len(words)
        result=[]

        for word in words:
            for ch in word:
                if ch not in indegree:
                    indegree[ch]=0
        
        for j in range(tword-1):
            w1=words[j]
            w2=words[j+1]

            if len(w1)>len(w2) and w1.startswith(w2):
                return ""
            
            for i in range(min(len(w1),len(w2))):
                if w1[i]!=w2[i]:
                    if w2[i] not in adjlist[w1[i]]:
                        adjlist[w1[i]].append(w2[i])
                        indegree[w2[i]]+=1
                    break
            
        queue=deque()

        for ch in indegree:
            if indegree[ch]==0:
                queue.append(ch)
            
        while queue:
                node=queue.popleft()
                result.append(node)
                
                for neg in adjlist[node]:
                    indegree[neg]-=1
                    if indegree[neg]==0:
                        queue.append(neg)
            
        if len(result)!=len(indegree):
            return ""
            
        return "".join(result)

# Time complexity is O(N × K + V + E) and space complexity is O(V + E)


# using dfs
from collections import defaultdict
class Solution:
    def findOrder(self, words):
        adjlist=defaultdict(list)
        visited=defaultdict(int)

        for word in words:
            for ch in word:
                if ch not in visited:
                    visited[ch]=0



        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j] and w2[j] not in adjlist[w1[j]]:
                    adjlist[w1[j]].append(w2[j])
                    break
        
        ans=[]

        def cycle(node):
            visited[node]=1

            for neg in adjlist[node]:
                # True its cycle
                if visited[neg]==1:
                    return True
                elif visited[neg]==0:
                    if cycle(neg):
                        return True
            
            visited[node]=2
            ans.append(node)
            return False
                
        
        for ch in visited:
            if visited[ch]==0:
                if cycle(ch):
                    return ""
        
        return "".join(reversed(ans))
        

# time compelxity is O(n*k + v*e) and space complexity is O(v+e)