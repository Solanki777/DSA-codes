def find_max_are(bottomleft,topright):
    max_area=0
    # by using brute force we find the all overlap parts

    # find all parts valid and invalid
    for i in range(len(topright)-1):
        for j in range(i+1,len(topright)):
            top=min(topright[i][1],topright[j][1])
            bottom=max(bottomleft[i][1],bottomleft[j][1])
            right=min(topright[i][0],topright[j][0])
            left=max(bottomleft[i][0],bottomleft[j][0])

            if top>bottom and right>left:
                # if we got ractange of 6*9 then their is 6*6 squre possible
                height=top-bottom
                width=right-left

                side=min(height,width)
                max_area=max(max_area,side**2)
    return max_area

bottomleft=[[1,1],[2,2],[3,1]]
topright=[[3,3],[4,4],[6,6]]
print(find_max_are(bottomleft,topright))