def check_leap(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    elif year%4==0:
        return True
    else:
        return False
def check_months(leap_year,num_month):
    """Here we are checking how many months are threre
    in a months.
    No matter if it's leap year or 
    not leap year."""
    if num_month>12 or num_month<1:
        print("Invalid output")
        
    else:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        if leap_year==True:
            if num_month==2:
                return months[1]+1
            else:
                return months[num_month-1]
        else:
            return months[num_month-1]
year=int(input("Enter the year:- "))
month=int(input("Enter the month:- "))
leap=check_leap(year)
days=check_months(leap_year=leap,num_month=month)
print(f"Number of days:- {days}")
