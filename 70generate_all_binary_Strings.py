ans=[]
def binary(index,l,flag):
    # initial case if we reache at the last
    if index==len(l):
        ans.append("".join(l))
        return
    
    # first apend "0" go to the left most part
    l[index]="0"
    binary(index+1,l,True)

    # after puting zero add "1" make flag false then we can only add "0" becuase we can not add "1" after other "1"
    if flag:
        l[index]="1"
        binary(index+1,l,False)
        l[index]="0"
n=3
l=[0]*n
print(l)
flag=True
binary(0,l,flag)
print(ans)

# time complexity is 2^N and space complexity is N