# my solution

# arr=[5,9,3,4,1]
# target=9
# ans=[]
# stack=[]

# def sub(arr,index,target):
#     if index>=len(arr):
#         temp_stack=stack.copy()
#         temp=0
#         while temp_stack:
#             temp+=temp_stack.pop()
#         if temp==target:
#             ans.append(stack.copy())
#             return
#         else:
#             return
#     stack.append(arr[index])
#     sub(arr,index+1,target)
#     stack.pop()
#     sub(arr,index+1,target)
# sub(arr,0,target)
# print(ans)

arr=[5,9,3,4,1]
target=9
ans=[]
stack=[]

def sub(arr,index,curr_sum,target):

    # if we got the sum  
    if curr_sum==target:
        ans.append(stack.copy())
        return
    
    # if we reaches the last element or sum is greer then target then no  need to go further
    if index==len(arr) or curr_sum>target:
        return 

    # include current elemtnt into the stack
    stack.append(arr[index])
    sub(arr,index+1,curr_sum+arr[index],target)
     
    # backtracing
    stack.pop()

    # exluce current elemtn
    sub(arr,index+1,curr_sum,target)

sub(arr,0,0,target)
print(ans)