string = "abcdefghijklmnopqrstuvwxyz"
alphabets = "abcdefghijklmnopqrstuvwxyz"

def encrypt(string):
    cipher_text = ""
    for i in range(len(string)):
        cipher_text += alphabets[-alphabets.index(string[i]) - 1]
    return cipher_text

def decrypt(cipher_text):
    plain_text = ""
    for i in range(len(cipher_text)):
        plain_text += alphabets[26 - alphabets.index(cipher_text[i])]
    return plain_text


print(encrypt(string))
print(decrypt(encrypt(string)))

