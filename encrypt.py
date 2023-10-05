alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    text_list = list(text)
    for num in range(len(text_list)):
        index = alphabet.index(text_list[num])
        text_list[num] = alphabet[index + shift]
    cipher_text = ""
    cipher_text = cipher_text.join(text_list)
    print(cipher_text)




    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"


plain_text = input("Please enter text to encrypt: ").lower()
shift_text = int(input("Enter the shift factor: "))
encrypt(text=plain_text, shift=shift_text)
