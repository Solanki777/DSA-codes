# my brute force mthod 

matrix=[[7,9,2,3],
        [20,8,0,10],
        [29,0,-10,5],
        [4,14,6,7]]

# here we have to find zero and set zeros to columans and rows of the place where the zero is found. like if zero is at [2][3] so 2 nd row and  3 column will bee full of zeros.

zero=float("inf")
row=len(matrix)
col=len(matrix[0])

for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            m,n=0,0
            while m!=row:
                matrix[m][j]=zero
                m+=1
            while n!=col:
                matrix[i][n]=zero
                n+=1
for i in range(row):
    for j in range(col):
        if matrix[i][j] == zero:
            matrix[i][j] = 0

print(matrix)

# otimal
        
