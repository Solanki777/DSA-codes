def spiral(matrix):
    if not matrix:
        return []
    
    else:
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        left=0

        result=[]

        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                result.append(matrix[top][i])

            top+=1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])

            right-=1

            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])

            bottom-=1

            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])

            left+=1
        
    return result
            


matrix=[[1,2,3,4,5,6],
        [20,21,22,23,24,7],
        [19,32,33,34,25,8],
        [18,31,36,35,26,9],
        [17,30,29,28,27,10],
        [16,15,14,13,12,11]]

ans=spiral(matrix)
print(ans)

# result should be [1,2,3,4,5,6,7,8,....36]

# time and space complexity is O(M*N)