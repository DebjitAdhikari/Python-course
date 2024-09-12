import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator\n")
num_letter=int(input("Enter how many letters "))
num_numbers=int(input("Enter how many numbers "))
num_symbols=int(input("Enter how many symbols "))
total=num_letter+num_numbers+num_symbols
password=[]
for i in range(0,num_letter):
        let=random.choice(letters)
        #password+=let
        password.append(let)
for i in range(0,num_numbers):
        no=random.choice(numbers)
        #password+=no
        password.append(no)
for i in range(0,num_symbols):
        sy=random.choice(symbols)
        #password+=sy
        password.append(sy)
print(password)
random.shuffle(password)
pas=""
for k in password:
    pas+=k
print(pas)