# using bfs traversal
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses==1:
            return [0]
        
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
            return []
        return result

# using dfs:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=[0]*numCourses
        adjlist=[[] for _ in range(numCourses)]
        ans=[]
        
        for u,v in prerequisites:
            adjlist[v].append(u)
        
        def cycle(node):
            visited[node]=1
            for neg in adjlist[node]:
                if visited[neg]==1:
                    return True
                if visited[neg]==0:
                    if cycle(neg):
                        return True
            
            visited[node]=2
            ans.append(node)
            return False


        for i in range(numCourses):
            if visited[i]==0:
                if cycle(i):
                    return []
        return ans[::-1]

# Time and space complexity is O(V+E )


        


        