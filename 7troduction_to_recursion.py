# Python is smart ? because if run any recursing having infinite calling than et some point arround 1000 it stops calling and thorugh an error that RecursionError: maximum recursion depth exceeded let example:

# def hello(i):
#     print(i)
#     hello(i+1)
# i=1
# hello(i)

# example 1: print Anirudh 4 time


i=0
def ani():
    global i
    if i==4:
        return
    print("Anirudh")
    i+=1
    ani()
ani()