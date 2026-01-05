def matrixsum(matrix):
    r=len(matrix)
    c=len(matrix[0])

    total=0
    neg=0
    mini=float("inf")

    for row in range(r):
        for col in range(c):

            total+=abs(matrix[row][col])
            mini=min(mini,abs(matrix[row][col]))

            if matrix[row][col]<0:
                neg+=1

    if neg%2==1:
        total-=2*mini
        return total
    return total


matix=[[-1]]
print(matrixsum(matix))