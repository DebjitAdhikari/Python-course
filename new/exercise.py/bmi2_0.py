height=float(input("Enter your height [in Meter]: "))
weight=float(input("Enter your weight [in KG]: "))
bmi=weight/(height**2)
bmi=round(bmi,2)
print("Your bmi :- ",bmi)
if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<25:
    print("You have normal weight")
elif bmi>=25 and bmi<30:
    print("You are overweight")
elif bmi>=30 and bmi<35:
    print("You are obese")
elif bmi>=35:
    print("You are Clinically obese")

