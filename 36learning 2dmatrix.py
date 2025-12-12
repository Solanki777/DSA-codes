# now we gona learn how the 2d matrix works.

twod_matrix=[[3,2,1],[2,3,4],[2,6,7]]

# here no of element in twod_matrix represents rows and no of element inside the element represents the no of column.

rows_of_twod=len(twod_matrix)
cols_of_twod=len(twod_matrix[0])

# 2d matrix is like=3,2,1
#                   2,3,4
#                   2,6,7

# as you can see above it is the example how the two d matrix is shown lets print it:
print("the matrix is : ")
for r in range(rows_of_twod):
    for c in range(cols_of_twod):
        print(twod_matrix[r][c],end=" ")
    print()

# now we gona find the sum of the matrix
total=0
for r in range(rows_of_twod):
    for c in range(cols_of_twod):
        total+=twod_matrix[r][c]
print("The sum of the matrix is :",total)


# Q1.print uppe trinagle:if you check the indexs of the uper triangle you find that r<=c each case so you can take it as you code

print("the uper triangle is :")
for r in range(rows_of_twod):
    for c in range(cols_of_twod):
        if r<=c:
            print(twod_matrix[r][c],end=" ")
        else:
            print("*",end=" ")
    print()

# Q2.print the lower triangle:

print("the lower triangle is :")
for r in range(rows_of_twod):
    for c in range(cols_of_twod):
        if r>=c:
            print(twod_matrix[r][c],end=" ")
        else:
            print("*",end=" ")
    print()

#Q3. print the diagonal

print("the diagonal is :")
for r in range(rows_of_twod):
    for c in range(cols_of_twod):
        if r==c:
            print(twod_matrix[r][c],end=" ")
        else:
            print("*",end=" ")
    print()

# Q4.transpose of the matrix:

# first we have to create a blank matrix which has rows and colmn opposite of the original matrix:
# this is how the blacnk transpose matrix is created:

result=[[0]*rows_of_twod for _ in range(cols_of_twod)]

print("the transpose matrix is : ")
for i in range(rows_of_twod):
    for j in range(cols_of_twod):
        result[j][i]=twod_matrix[i][j]
print(result)

# other way to get transpose of the matrix is

matrix=[
    [1,2,3],
    [4,5,6]
]

rows=len(matrix)
cols=len(matrix[0])

transpose=[]
print("transpose of the matrix is :")
for i in range(cols):
    new_row=[]
    for j in range(rows):
        value=matrix[j][i]
        new_row.append(value)
    transpose.append(new_row)
print(transpose)

