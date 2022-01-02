from logos import cipher_logo

print(cipher_logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def cesar(start_text, shift_amt, cipher_direction):
    new_text = ""

    if cipher_direction == "d":
        shift_amt *= -1
    for i in start_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amt
            new_text += alphabet[new_position]
        else:
            new_text  += i

        # try:
        #     position = alphabet.index(i)
        #     new_position = position + shift_amt
        #     new_text += alphabet[new_position]
        # except:
        #     new_text += i
    print(f"Here is the {cipher_direction}d result: {new_text}")



keep_going = True
while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    print(shift)

    if direction == "e" or direction == "d":
        cesar(start_text=text,cipher_direction=direction,shift_amt=shift)
    else:
        print("Invalid direction")

    k=input("Type 'yes' if you want to go again.  Otherwise type 'no': ").lower()
    if k == "no":
        keep_going = False

print("Goodbye")
