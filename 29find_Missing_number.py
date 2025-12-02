# here you have the arry is given 
# a=[0,8,6,5,4,1,2,3,9] as here from 0 to 9 but 7 is missing so we have to return the missing element


def m(arr):
    max=arr[0]
    min=arr[0]
    for el in range(1,len(arr)):
        if arr[el]>max:
            max=arr[el]
        elif arr[el]<min:
            min=arr[el]

    print("maximum number from arry is ",max)
    print("minimum number number from arry is ",min)

# so now we have the limit between uper and lower side
    temp=[]
    for el in range(min,max+1):
        temp.append(el)
        
    print(temp)
    print(arr)

    for el1 in temp:
        n_found=True
        for el2 in arr:
            if el1==el2:
                n_found=False
                break
        if n_found:
            return el1

            

    

arr=[0,8,6,5,4,1,2,3,9]
ans=m(arr)
print("the missing elements is ",ans)