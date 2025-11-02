# let n=[4,7,8,5,6,1,2,5,4,7,8,5,9,6]
# and m=[1,2,3,4,5,6,7,8,9]

# here the concept is if the element is found in n of m than the count of m for particualr elemenet is increces.for example there 1 for 1 time than 2 for 1 time also 

# n=[4,7,8,5,6,1,2,5,4,7,8,5,9,6]
# m=[1,2,3,4,5,6,7,8,9]

# for i in m:
#     count=0
#     for j in n:
#         if i==j:
#             count +=1
#     print(count)

    # here the loop runs for m and other for n so the time complexity is n*m which where large if m and n has 10^8 element than it program execution throws an error that shows Time Limit Exceed(TLE) where operation goes out of 10^8 operations 

    # Optimal solution: here we can make an empty error of size max of n. Like n's element is exites than increase the vlaue in empty error 
    # it start from 4 so it increses the value at index for in new empty error


# n=[4,7,8,0,5,6,1,2,5,4,7,8,5,9,6]
# m=[0,1,2,3,4,5,6,7,8,9]

# empty=[0]*10 #which make an empty array of size 10 form 0 to 9 because maximum elemnt is 9 and minimum element is 1


# for el in n:
#     empty[el]+=1

# for ele in m:
#     if ele<0 or ele>9:
#         print(0)
#     else :
#         print(empty[ele])

# here time complexity becomes m+n not m*n which is way mor efficient
# lets try with dictonary to store the values because here we assume what are the maximum and minimum number which range help us to make conditions and store the frequncy .But what if the number is n are random than what should you do?

# n=[4,7,8,0,5,6,1,2,5,4,7,8,5,9,6]

# emty_freq_map=dict()

# for el in n:
#     emty_freq_map[el]=emty_freq_map.get(el,0)+1
# print(emty_freq_map)

# so this will prints the freqency that really exits in n 

# lets go in string where m="asdfasdfdghfjfghdasdh" and n=["a","s","d","f","g","h","j"]
# here the thing is same but for Makig empty array first we convert the charcheter into ASCII means ASCII of a is 97 like that than minus 97 it means 0 th index . So this is how we strore the frequency of a.

m="asdfasdfdghfjfghdasdh"
n=["a","s","d","f","g","h","j"]
d=dict()

for el in m:
    asci=ord(el)
    index=asci-97
    d[index]=d.get(index,0)+1
for el in n:

print(d)

# using ASCII you can perform a string having captial,small alphabets and with special sybols if you know the ascii values
