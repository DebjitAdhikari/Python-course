shoppingList=["Cocacola","Butter","Milk","Apples"]
print(shoppingList)
del shoppingList[1] #"del" function will delete the element
print(shoppingList)
#--------------------------------------
arr1=[23,55,49]
arr2=[48,88]
arr3=arr1+arr2
print(arr3)
#=-------------------------
len(shoppingList)# "len" function helps to print the lenth of any array
print("The lenth of the array",len(shoppingList))
print(len(arr3))
#---------------------------------
num=[39,333,20003,-44,53]
max(num)  #"max" function helps to find max value of an array
print("The maximum value of the array",max(num))
#--------------------------------------------
min(num) #"min" function helps to find minimum value of an array
print("The minimum value of the array is",min(num))
#-----------------------------------------------
shoppingList.count("Milk")  #"count" function helps to count frequency
print("the frequency of milk is",shoppingList.count("Milk"))
