#global scope
# a=10
# def pr():
#     print(a)
# pr()

#there is no block scope in python

# if True:
#     a=10
# print(a) #variables that are created inside block can be acessable out side of the block

# def di():
#     if True:
#         a=10
#     print(a)
# di()

# modifying global variable
a=10
def something():
    global a #it will allow to modify the global variable
    a+=1
    print(f"from inside: {a}")
something()
print(f"from outside: {a}")

#global constants
PI= 3.14