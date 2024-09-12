def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+":add,  #key values can contain the name of the function after
              # the function declearation 
    "-":sub,
    "*":multiply,
    "/":div
}
first=int(input("Enter the first: "))
opt=input("enter the operator: ")
sec=int(input("Enter the second: "))
which_function=operations[opt]
print(which_function(first,sec))
