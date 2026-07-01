# 3. Representation in DSA
#     Adjacency Matrix
#     2D array
#     matrix[i][j] = 1 if edge exists else 0
    #   if i==0 or j==0 or i==j then then matrix[i][j]=0
# example:
# node=5
# vertices=6

# connextion=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# matrix=[[0 for _ in range(node+1)] for _ in range(node+1)]

# for u,v in connextion:
#     matrix[u][v]=1
#     matrix[v][u]=1

# print(matrix)

# if you given weight tha put it instead of 1 











    # you given n edges so build empty matrix of (n+1)*(n+1) then fill it
# node=5
# vertices=6

# connextion=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# lst=[[] for _ in range(node+1)]
# # print(lst)

# for u,v in connextion:
#     lst[u].append(v)
#     lst[v].append(u)
# print(lst)

# for fetching elements from lst takes O(1)




#     Adjacency List/dictionary (most used)
#     Each node stores list of neighbors
#     graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0],
#     3: [1]
#     }


# if you given weight than it like:
# 1->[[2,3]]

# where 1 is connected with wirght 3




# if you use dictionary instead of lst it may take O(n) if very rear (which know as amortised worst case (once in moves))  so using dictionary is node preferable
# node=5
# vertices=6

# connextion=[[1,2],[2,4],[3,4],[1,3],[3,5],[5,4]]

# my_dict={}
# for i in range(1,node+1):
#     my_dict[i]=[]

# # print(my_dict)

# for u,v in connextion:
#     my_dict[u].append(v)
#     my_dict[v].append(u)

# print(my_dict)



# if there is directed graph than put values only if there is directed incomming edge else zero 


