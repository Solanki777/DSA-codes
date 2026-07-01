arr=[5,7,9]
stack=[]
ans=[]
def sub(stack,index):
    if index>=len(arr):
        ans.append(stack.copy())
        return
    
    stack.append(arr[index])
    sub(stack,index+1)
    stack.pop()
    sub(stack,index+1)

sub(stack,0)
print(ans)