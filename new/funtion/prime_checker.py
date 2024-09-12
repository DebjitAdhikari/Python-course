def prime_checker(n):
    flag=0
    half=int(n/2)
    for i in range(2,half):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print("This is a prime number")
    else:
        print("This is not a prime number")
number=int(input("Enter a number to check prime or not "))
prime_checker(n=number)
