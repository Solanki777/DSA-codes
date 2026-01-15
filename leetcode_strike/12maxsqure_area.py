hbars=[2,3,4]
vbars=[1,2,3,5,6]

hbars.sort()
vbars.sort()
counth=1
countv=1
maxh=1
maxv=1

for i in range(len(hbars)-1):
    if hbars[i+1]==hbars[i]+1:
        counth+=1
    else:
        maxh=max(counth,maxh)
        counth=1
maxh=max(counth,maxh)    

for i in range(len(vbars)-1):
    if vbars[i+1]==vbars[i]+1:
        countv+=1
    else:
        maxv=max(countv,maxv)
        countv=1
maxv=max(maxv,countv)
side=min(maxh,maxv)+1

area=side*side

print(area)
