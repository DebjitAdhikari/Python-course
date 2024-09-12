# 👎🤢
# import csv
# with open("weather_data.csv")as file:
#     data=csv.reader(file)
#     temperature=[]
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# 👍😊
# in pandas the whole data table is called 'dataframe' 
# and each column is called 'series' it's kind of like 'list' in python
import pandas
data=pandas.read_csv("weather_data.csv")
print(data["temp"])
# data_dict=data.to_dict()
# print(data_dict)
# data_list=data["temp"].to_list()
# print(data_list)
# # avg_temp=sum(data_list)/len(data_list)
# # print(avg_temp)

# print(data["temp"].mean())
# print(data["temp"].max())

# #get data in columns
# print(data["temp"])
# print(data.temp)

# get data from rows
#          once a particular condition qualifies the criteria then it return the data of that row
# print(data[data.day=="Monday"])
# print(data[data.temp == data.temp.max()])

monday= data[data.day=="Monday"]
monday.temp


