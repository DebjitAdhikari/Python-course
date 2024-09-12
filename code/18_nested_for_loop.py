for i in range(0,5):
    for a in range(0,5):
        print(a)
# first 10 prime numbers
print("First 10 prime numbers are")
for i in range(1,11):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==0:
        print(i)