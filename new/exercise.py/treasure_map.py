row1=["🫥", "🫥", "🫥"]
row2=["🫥", "🫥", "🫥"]
row3=["🫥", "🫥", "🫥"]
mapp=[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure ")
column=int(position[0])
row=int(position[1])
#select_row=map[column-1]
#select_row[row-1]="X"
mapp[row-1][column-1]="X"
print(f"{row1}\n{row2}\n{row3}")