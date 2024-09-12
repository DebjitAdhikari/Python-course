my_visit=[
    {
    "country":"India",
    "total_visited":3,
    "visted":["Delhi","Kolkata","Bangalore"],
    }
]
def add_new_country(name,total,list):
     new_country={}
     new_country["country"]=name
     new_country["total_visited"]=total
     new_country["vistied"]=list
     my_visit.append(new_country)
add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(my_visit)