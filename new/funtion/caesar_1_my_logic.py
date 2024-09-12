alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(msg,numbers):
    limit=len(alphabet)-numbers
    encrypted_msg=msg
    msg_size=len(msg)
    for i in range(0,len(alphabet)):
            for j in range(0,msg_size):
                if alphabet[i] in msg[j]:
                     if i<limit:
                        encrypted_msg[j]=alphabet[i+numbers]
                     else:
                         encrypted_msg[j]=alphabet[i]
    print(msg)

        

direction=input("ENter 'encode' to make and 'decode' to decode your message:- ")
message=input("Enter your message:- ").lower()
shift=int(input("Enter the shift number:- "))
my_msg=[]
for i in message:
    my_msg+=i
encrypt(msg=my_msg,numbers=shift)