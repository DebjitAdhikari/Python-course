# 1st way .........
# file = open("my.txt")
# contents=file.read()
# print(contents)
# file.close()

# 2nd way...........
# with open("my.txt") as file:
#     contents=file.read()
#     print(contents)

# 'a' for append, 'w'for write, 'r' read

# changes the text file content 
# with open("my.txt", mode="w") as myfile:
#     myfile.write("Hey whats up?")

# adding some new text line
# with open("my.txt",mode="a") as myfile:
#     myfile.write("\nDEbjit")
#     myfile.write("\nADhikar")

# if file doesn't exist then it creates new file
with open("new.txt",mode="a") as myfile:
    myfile.write("\nDEbjit")
    myfile.write("\nit's new file")
