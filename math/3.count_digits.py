def countDigits(n: int) -> int:
    temp=n
    count=0
    while temp>0:
        i=temp%10
        if i==0:
            temp=temp//10
            continue
        elif n%i==0:
            count+=1
        temp=temp//10
    return count


# time complexity is O(logn) and space complexity is O(1)