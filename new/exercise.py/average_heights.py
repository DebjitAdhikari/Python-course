height=input("Enter the list of students height:- ").split()
for i in range(0,len(height)):
    height[i]=int(height[i])
print(height)
d=0
sum=0
for j in range(0,len(height)):
    sum=sum+height[j]
    d=d+1
average=int(sum/d)
print("The average height is ", average)