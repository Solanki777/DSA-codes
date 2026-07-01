# 1. using kahn's algorithm BFS traversal 
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        queue=deque()
        result=[]

        for u,v in prerequisites:
            adjlist[v].append(u)
            indegree[u]+=1
        
       
            
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            currnode=queue.popleft()
            result.append(currnode)
            for neg in adjlist[currnode]:
                indegree[neg]-=1
                if indegree[neg]==0:
                    queue.append(neg)
        if len(result)!=numCourses:
            return False
        else:
            return True

# using dfs 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist=[[] for _ in range(numCourses)]
        visited=[0]* numCourses

        for u,v in prerequisites:
            adjlist[v].append(u)
        
        def cycle(node):
            visited[node]=1
            for neg in adjlist[node]:
                if visited[neg]==1:
                    return True
                elif visited[neg]==0:
                    if cycle(neg):
                        return True

                
            visited[node]=2
            return False         
        
        for i in range(len(visited)):
            if visited[i]==0:
                if cycle(i):
                    return False
        return True

# Time and space complexity is O(V+E )


