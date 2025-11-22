# def mover(arr):
#     l=len(arr)
#     i=0
#     new_arr=[]
#     zero_arr=[]
#     for el in range(l):
#         if(arr[el]!=0):
#             new_arr.append(arr[el])
#             i+=1
#         else:
#             zero_arr.append(0)
#     arr[:]=new_arr+zero_arr
#     print(arr) 

# arr=[1,0,2,4,3,0,0,3,5,1]
# mover(arr)

# here the time complexity is O(2N) . One N for findng non-zeros in arry and other for for concating both arry so overall it will become O(N). And space complexity will be O(N) for distict arr

# optimal solution

# in optimal soution we taking 2 variable named i and j . i will find zeros in arr when it finds the zero j loop runs to find non-zero element if it does than swap the ith and jth value

def mover(arr):
    i=0
    if(len(arr)==1):
        return
    while(i<len(arr)):
        if(arr[i]==0):
            break
        i+=1
    if(i==len(arr)):
        return
    
    j=i+1
    while(j<len(arr)):
        if(arr[j]!=0):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        else:
            j+=1
    return arr
arr=[1,2,3,4,0,2,4,3,0,0,3,5,1]
ans=mover(arr)
print(ans)

# Here the time compelexity is same but space complexity would be 1