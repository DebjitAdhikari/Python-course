my_dict={
    "Name":"DEbjit",
    "title":"Adhikari",
    "job":"unemployed",
}

# print(my_dict)
# print(my_dict["title"])

#adding in dictionaries
# my_dict["duty"]="student"
# print(my_dict)

#creating a empty dictionaries
# my_new_dict={}

#wiping data of a exicting dictionaries
# my_dict={}

#edit an item in a dictionary
# my_dict["job"]="got placed"
# print(my_dict)

#looping through the dictionaries
for i in my_dict:
    print(i) #prints the key
    print(my_dict[i])   #prints the value

#nesting a dictionary in a dictionary
travel_log={
    "France":{
        "cities_visited":["Paris","lille","dijon"],
        "total_visits":12
        },
    "Germany":{
        "cities_visited":["berlin","hamburg","stuttgart"],
        "total_visits":5
        },
}

#nesting dictionary in a list
travel_log=[
    {
        "country":"France",
        "cities_visited":["Paris","lille","dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["berlin","hamburg","stuttgart"],
        "total_visits":5
    },
]