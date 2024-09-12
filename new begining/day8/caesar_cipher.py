alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end=False
def cipher(command,text,shift):
        msg=""
        for i in text:
            if i in alphabet:
                ind=alphabet.index(i)
                if command=="encode":
                    msg+=alphabet[ind+shift]
                else:            
                    msg+=alphabet[ind-shift]
            else:
                msg+=i
        print(f"The {command}d message is: {msg}") 

while not end:
    command=input("Type 'encode', 'decode' or 'exit': ").lower()
    if command=="exit":
        break
    text=input("Enter the your text: ")
    shift=int(input("Enter the shift amount: "))
    cipher(command,text,shift)