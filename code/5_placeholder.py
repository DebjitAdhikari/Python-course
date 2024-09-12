#Suppose I want to invite some friends in my birthday, to make it lot easier
#We use  placeholder as a template;
sen="Hello %s, you're invited to my birthday"
print(sen%("Deb"))
print(sen%('Sushmita'))
arr=["Levi","Kakashi","Peter"]
for i in arr:
    print(sen%(i))
pla="Hey %s, you're not invited to my birthday"
soo=["John","Mike","Joseph"]
for j in soo:
    print(pla%(j))
ann="Hello %s %s, welcome to my party"
print(ann%("Debjit","Adhikari"))
#new=["Debjit","Dev","Jonas"]
#ano=["Adhikari","Thompson","Anderson"]
#for k in new:
#    for j in ano:
#      print(ann%(k,j))
det="Hello I am %s and my age is %d"
print(det%("Debjit Adhikari",17))