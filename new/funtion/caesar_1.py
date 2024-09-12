from caesar_art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(msg,numbers,code):
    cipher_text=""
    for letters in msg:
         if letters in alphabet:
             position=alphabet.index(letters)
             if code=="encode":
                 new_position=position+numbers
             elif code=="decode":
                new_position=position-numbers
             cipher_text+=alphabet[new_position]
         else:
             cipher_text+=letters    
    print(f"Your {code}d Cipher text is {cipher_text}")
end_of_program=False
while not end_of_program:
    direction=input("Enter 'encode' to create and 'decode' to decode your message:- ")
    message=input("Enter your message:- ").lower()
    shift=int(input("Enter the shift number:- "))
    new_shift=shift%len(alphabet)
    my_msg=[]
    for i in message:
        my_msg+=i
    cipher(msg=my_msg,numbers=new_shift,code=direction)
    loop=input("Type 'Yes' to run again, type 'No' to exit:- ").lower()
    if loop=="no":
        print("Goodbye.")
        end_of_program=True

