# Python is smart ? because if run any recursing having infinite calling than et some point arround 1000 it stops calling and thorugh an error that RecursionError: maximum recursion depth exceeded let example:

# def hello(i):
#     print(i)
#     hello(i+1)
# i=1
# hello(i)

# example 1: print Anirudh 4 time

# head recursion:When i reaches to 4 it will retrun to preivious function who call tham and check any part of that function is remain for execution or not if yes then it will execute it and go back to the called funtion
# i=0
# def ani():
#     global i
#     if i==4:
#         return
#     print("Anirudh")
#     i+=1
#     ani()
# ani()

# example 2:print Anirudh 4 time

# tail recursion:here it will call the same function 4 times and than after each call the funcion is push the called function into the stack after reaching at i==4 it says retuqn so it will pop those fuction which are stored in the stack and go for that function if there is any reaminng code to run it will runs it 
i=0
def ani():
    global i
    if i==4:
        return
    i+=1
    ani()
    print("Anirudh")
ani()

# Time complexity is O(n+1)   for calling that funtion by funcion it self and starting call and return.
# time complextity becomes O(n) by ignorring 1
# Same as in space the all values are storing in the stackbase by function is self is n times and in startin the first time call so Space compelxity is O(n+1) Which is approximately O(n)