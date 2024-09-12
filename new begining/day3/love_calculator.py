you=input("What's your name:")
her=input("what's her name")
fullname=(you+her).lower()
t=fullname.count("t")
r=fullname.count("r")
u=fullname.count("u")
e=fullname.count("e")
tr=t+r+u+e

l=fullname.count("l")
o=fullname.count("o")
v=fullname.count("v")
e=fullname.count("e")
lov=l+o+v+e
print(f"YOur love:{tr}{lov}")