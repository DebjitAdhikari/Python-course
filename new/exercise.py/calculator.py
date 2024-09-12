from calculator_art import logo
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":div,
}
def calculator():
    print(logo)
    num1=float(input("Enter the first number:- "))
    for operands in operations:
        print(operands)
    end_of_program=False
    while not end_of_program:
        equation=input("Pick an operation:- ")
        fun=operations[equation]
        num2=float(input("Enter the next number:- "))
        result=fun(num1,num2)
        print(result)
        ans=input("Type 'y' to continue and 's' to start a new calculation:- ").lower()
        if ans=="y":
            num1=result
        else:
            end_of_program=True
            calculator()
calculator()