# Tuples elements can't be edited, deleted. It can be replaced
tup=("maths",66,"dogs")
print(tup)
# tup.append("cat")  it will never work
# del tup["maths"]  it not correct
tup=("cat") # it can be replaced
print(tup)
tup=("maths",66,"dogs")
print(tup[0])  # we can access any element of tuples by it's index 
print(tup[0:3])
del tup
print(tup)