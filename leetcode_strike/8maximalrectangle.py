
def max_rectangle(matrix):
    m=len(matrix)
    n=len(matrix[0])
    ans=0
    for i in range(m):
        lst=[]
        for j in range(n):
            if i==0:
                lst.append(matrix[i][j])
            elif matrix[i-1][j]!=matrix[i][j]:
                lst.append(matrix[i][j])
            else:
                
                lst.append(matrix[i-1][j]+matrix[i][j])
        ans=max(ans,solve(lst))
    
    return ans
    
def solve(lst):
    stack=[]
    max_are=0
    for i in range(len(lst)):
        while stack and lst[i]<lst[stack[-1]]:
            h=lst[stack.pop()]        
            w=i if not stack else i-stack[-1]-1
            max_are=max(max_are,h*w)
        stack.append(i)
    
    
    return max_are


matrix=[[0,1,1,0],
        [1,0,0,1],
        [1,1,1,0],
        [0,1,1,1]]

print(max_rectangle(matrix))