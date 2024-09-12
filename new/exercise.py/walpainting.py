import math
def can_print(h,w,s):
    can=(h*w)/s
    can=math.ceil(can)
    print(f"You need {can} cans to print")
height=int(input("Enter the height of your wall "))
width=int(input("Enter the width of your wall "))
# one can only print 5 square so 
can_square=5
can_print(h=height,w=width,s=can_square)