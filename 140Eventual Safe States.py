# using bfs 
# if we think than here we have to ignore cycle which we seen in topological sorting
# also the involve or going in cycle also we have to ignore so after cycle edges comes inside the cycle we have to ignor

# if we apply topo logical sorting it ignores cycle but not ingoing edges iside the cycle so first we reverse the all node 

# than apply the topological sorting 

# using bfs 

from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adjlist=[[] for _  in range(len(graph))]
        queue=deque()
        indegree=[0]*len(graph)
        result=[]

        for l in range(len(graph)):
            for el in graph[l]:
                adjlist[el].append(l)
                indegree[l]+=1
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            curr_node=queue.popleft()
            result.append(curr_node)

            for neg in adjlist[curr_node]:
                indegree[neg]-=1
                if indegree[neg]==0:
                    queue.append(neg)
        
        return sorted(result)
# time and space complexity is O(V+E)


# using dfs
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjlist=[[] for _ in range(len(graph))]
        visited=[0]*len(graph)
        resutl=[]

        adjlist=graph

        def dfs(node):
            visited[node]=1

            for neg in adjlist[node]:
                if visited[neg]==0:
                    if dfs(neg):
                        return True
                    
                elif visited[neg]==1:
                    return True
            
            resutl.append(node)
            visited[node]=2
            return False

        for i in range(len(visited)):
            if visited[i]==0:
                if dfs(i):
                    continue
        
        return sorted(resutl)

# time compelxity is O(V+E) and space complexity is O(V)

        