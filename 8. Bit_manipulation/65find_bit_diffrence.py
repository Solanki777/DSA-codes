start=10
goal=7

temp=start ^ goal

count=0
for i in range(32):
    if temp&(1<<i):
        count+=1
print(count)