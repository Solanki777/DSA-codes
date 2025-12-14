# my brute force mthod 

# matrix=[[7,9,2,3],
#         [20,8,0,10],
#         [29,0,-10,5],
#         [4,14,6,7]]

# # here we have to find zero and set zeros to columans and rows of the place where the zero is found. like if zero is at [2][3] so 2 nd row and  3 column will bee full of zeros.

# zero=float("inf")
# row=len(matrix)
# col=len(matrix[0])

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j]==0:
#             m,n=0,0
#             while m!=row:
#                 matrix[m][j]=zero
#                 m+=1
#             while n!=col:
#                 matrix[i][n]=zero
#                 n+=1
# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == zero:
#             matrix[i][j] = 0

# print(matrix)

# time coplexity is O(n^3) if it hase same length of raw and diagonal

# otimal : here we taking two arry for raw trac and column track . First we iterate the matrix if zero is found then mark -1 in then raw and column respectilvy.

def setzero(matrix):
    raw=len(matrix)
    col=len(matrix[0])

    raw_trac=[0]*raw
    col_trac=[0]*col

    for i in range(raw):
        for j in range(col):
            if matrix[i][j]==0:
                raw_trac[i]=-1
                col_trac[j]=-1

    print(raw_trac)
    print(col_trac)

    # now we have the location that where the zero comes

    for i in range(raw):
        for j in range(col):
            if raw_trac[i]==-1 or col_trac[j]==-1:
                matrix[i][j]=0
    return matrix


# here the time complexity is O(raw*col) and space coplexity is O(raw+col)


matrix=[[7,9,2,3],
        [20,8,0,10],
        [29,0,-10,5],
        [4,14,6,7]]

ans=setzero(matrix)
print(ans)