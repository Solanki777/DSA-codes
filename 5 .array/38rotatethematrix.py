# brute force solution my solution
# def rotate(matrix):
#     raw=len(matrix)
#     col=len(matrix[0])
    
#     new_matrix=[]
#     for j in range(col):
#         temp=[]
#         for i in range(raw-1,-1,-1):
#             temp.append(matrix[i][j])
        
#         new_matrix.append(temp)
    
#     print(new_matrix)

# time complexity is O(R*C) and space complexity is also O(R*C)




# matrix=[[1,2,3,4],
#         [5,6,7,8],[9,10,11,12],[13,14,15,16]]
# ans=rotate(matrix)
# print(ans)
# here we have to rotate the matrix by 90 degree 


# otimal solution
# here we first gona transpose of the matrix

# matrix=[[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,10],
#         [13,14,15,16]
#         ]

# our actual answer=[[13, 9, 5, 1], 
#                    [14, 10, 6, 2],
#                    [15, 11, 7, 3], 
#                    [16, 12, 8, 4]]

# trnaspose of the matrix=[[1,5,9,13],
#                          [2,6,10,14],
#                          [3,7,11,15],
#                          [4,8,10,16]]

# to get transpose you can see and diagonal remains same
# [0][1]=[1][0]
# [0][2]=[2][0]
# [0][3]=[3][0]
# [1][2]=[2][1]
# [1][3]=[3][1]
# [2][3]=[3][2]

# if we revese the each raw than we got the solution if we assume first one is i than it goes from 0 to 2 which is raw-1 and 

def rotate(matrix):
    # first we gona transpose of the matrix

    # in transpose diagonal remain same
    raw=len(matrix)
    col=len(matrix[0])

    for i in range(raw-1):
        for j in range(i+1,raw):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    # transpose
    print(matrix)

    for r in range(raw):
        i=0
        j=col-1
        while(i<j):
            matrix[r][i],matrix[r][j]=matrix[r][j],matrix[r][i]

            i+=1
            j-=1

    print(matrix)




matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,10],
        [13,14,15,16]
        ]
ans=rotate(matrix)

