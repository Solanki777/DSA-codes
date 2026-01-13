squares=[[0,0,4],[2,1,2],[1,4,3]]

# find the lower part and upper part
l=len(squares)
lower=float("inf")
higher=float("-inf")


for i in range(l):
    bottom=squares[i][1]
    top=squares[i][1]+squares[i][2]

    if lower>bottom:
        lower=bottom
    
    if higher<top:
        higher=top

# used to calculate mid in future
low=lower
high=higher

for _ in range(60):
    mid=(low+high)/2

    above_line=0
    below_line=0
    
    # finding area above and below the mid line 
    for i in range(l):
        b=squares[i][1]
        t=squares[i][1]+squares[i][2]
        length=squares[i][2]

        # squre is above  the line 
        if b>=mid:
            above_line+=length*length
        
        # squre is below the line
        elif mid>=t:
            below_line+=length*length
        
        # line cuts the squre
        else:
            above_line+=length*(t-mid)
            below_line+=length*(mid-b)
    
    # new higher and lower
    if below_line<above_line:
        low=mid
    else:
        high=mid
answer=(low+high)/2
print(answer)
    






