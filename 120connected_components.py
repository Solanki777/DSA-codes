# Think of a graph as a network of cities connected by roads.
# A connected component is a set of cities where you can travel between any two cities using the roads, but you cannot reach cities outside that set.

# Example

# If a graph has nodes:

# A — B — C     D — E     F


# to traverse above like graph we require visited list where we put 1 where where we visit the node 

from collections import deque
class Solution:
    def component(self,lst):
        def traverse(lst,visited,node):
            queue=deque([node])
            visited[node]=1
            while queue:
                current=queue.popleft()
                for i in lst[current]:
                    if visited[i]==0:
                        queue.append(i)
                        visited[i]=1
            
        vist=[0]*(len(lst))
        count=0
        
        for i in range(1,len(vist)):
            if vist[i]==0:
                count+=1
                traverse(lst,vist,i)
        return count

lst = [
    [],        # 0 (unused)
    [2],       # 1 → connected to 2
    [1, 3],    # 2 → connected to 1, 3
    [2],       # 3 → connected to 2
    [5],       # 4 → connected to 5
    [4],       # 5 → connected to 4
    []         # 6 → isolated node
]

sol = Solution()
print(sol.component(lst))              
