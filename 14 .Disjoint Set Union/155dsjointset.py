# using rank 
class Disjointset:
    def __init__(self,n):
        self.parent=[i for i in range(0,n+1)]
        self.rank=[0]*(n+1)
    
    def ultiparent(self,node):
        if node==self.parent[node]:
            return node
        
        self.parent[node]=self.ultiparent(self.parent[node])

        return self.parent[node]
    
    def union(self,u,v):
        pu=self.ultiparent(u)
        pv=self.ultiparent(v)

        if pu==pv:
            return 
        
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        
        elif self.rank[pv]<self.rank[pu]:
            self.parent[pv]=pu
        
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

ds=Disjointset(7)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)

print(ds.ultiparent(1))
print(ds.ultiparent(2))

# By using rank we can only assume than how many height of  graph was we can not find how many nodes are there so now we using size 


# using size 
class Disjointset:
    def __init__(self,n):
        self.parent=[i for i in range(0,n+1)]
        self.size=[1]*(n+1)
    
    def ultiparent(self,node):
        if node==self.parent[node]:
            return node
        
        self.parent[node]=self.ultiparent(self.parent[node])

        return self.parent[node]
    
    def union(self,u,v):
        pu=self.ultiparent(u)
        pv=self.ultiparent(v)

        if pu==pv:
            return 
        
        if self.size[pu]<self.size[pv]:
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        
        elif self.size[pv]<self.size[pu]:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]

ds=Disjointset(7)

ds.union(1,2)
ds.union(2,3)
ds.union(4,5)
ds.union(6,7)
ds.union(5,6)
ds.union(3,7)

print(ds.ultiparent(1))
print(ds.ultiparent(2))

# Why we connect smaller graph to bigger graph?
# to reduce time complextiy if put bigger graph under smaller than in path compression we have to travers bigger graph and change all ultimate parets which takes more time than this that's why

# Time complexity is O(1) for more practically it is O(alfa(n)) and space complexity is O(n)