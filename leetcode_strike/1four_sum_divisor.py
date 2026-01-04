def sum4divisor(nums):
    total=0
    for el in nums:
        s=0
        count=0
        i=1
        while i<=el**0.5:

            if el%i==0:
                other=el//i
                count+=1
                s+=i

                if i!=other:
                    count+=1
                    s+=other

            if count>4:
                break
        
            i+=1
        if count==4:
            total+=s

    return total

print(sum4divisor([36,21,4,7]))