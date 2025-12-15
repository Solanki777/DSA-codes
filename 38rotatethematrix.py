# brute force solution my solution
def rotate(matrix):
    raw=len(matrix)
    col=len(matrix[0])
    
    new_matrix=[]
    for j in range(col):
        temp=[]
        for i in range(raw-1,-1,-1):
            temp.append(matrix[i][j])
        
        new_matrix.append(temp)
    
    print(new_matrix)

# time complexity is O(R*C) and space complexity is also O(R*C)




matrix=[[1,2,3,4],
        [5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans=rotate(matrix)
print(ans)
# here we have to rotate the matrix by 90 degree 


# otimal solution



