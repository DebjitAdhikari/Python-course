students=["Eric",12,"Bob",14,"Joey",43]
students={"Eric":12,"Bob":14,"Joey":43}
students["Bob"] # it will print the  Where Eric is Key and after : is value
print("The age of Bob is",students["Bob"])
students["Bob"]=20
print("The updated age of bob is ",students["Bob"])
del students["Bob"]  #it is case sensetive
print(students)