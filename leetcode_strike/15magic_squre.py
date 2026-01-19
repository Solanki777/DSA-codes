def is_magic(i,j,max_size,row_prefix,col_prefix,grid):
    # find the sum from the row_prefix table
    target=row_prefix[i][j+max_size]-row_prefix[i][j]

    # check raw sum
    for r in range(i,i+max_size):
        if row_prefix[r][j+max_size]-row_prefix[r][j]!=target:
            return False
    
    # check colum sum
    for c in range(j,j+max_size):
        if col_prefix[i+max_size][c]-col_prefix[i][c]!=target:
            return False
    
    # check diagonal
    diag1=0
    for d in range(max_size):
        diag1+=grid[i+d][j+d]
    if diag1!=target:
        return False
    
    diag2=0
    for d in range(max_size):
        diag2+=grid[i+d][j+max_size-1-d]
    if diag2!=target:
        return False
    return True



def possible_squre(grid):

    m=len(grid) #rows
    n=len(grid[0]) # cols
    
    # build row and column prefix
    row_prefix=[[0]*(n+1) for _ in range(m)] # extra column
    col_prefix=[[0]*(n) for _ in range(m+1)] # extra row

    # now fill the answer of sum
    for i in range(m):
        for j in range(n):
            row_prefix[i][j+1]=row_prefix[i][j]+grid[i][j]
            col_prefix[i+1][j]=col_prefix[i][j]+grid[i][j]
    
    # maximum the squrre we got
    max_size=min(m,n)

    # find the all possible squre are build in the grid send them to other function which check the squre is magic or not
    while (max_size>=2):
        for i in range(m-max_size+1):
            for j in range(n-max_size+1):
                if is_magic(i,j,max_size,row_prefix,col_prefix,grid):
                    return max_size
        max_size -=1
    return 1

    
    






grid=[[5,1,9,1],[9,3,3,1],[1,3,3,8]]

possible_squre(grid)

