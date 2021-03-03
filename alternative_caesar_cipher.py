def decrypt(text):
    print("message 1")
    for i in range(26):
        for j in text:
             k = (ord(j) + i)
             if k > 122:
                 k = k - 26
             print(chr(k))
        print("message", i + 2)
        #zkc

def encrypt(text, key):
    pass

running = True
while running:

    option = int(input("Please enter: 1 to decrypt, 2 to encrypt "))

    if option == 1:
        decrypt_message = str(input("Enter the secret message to decrypt..."))  # aktgjakcafyqwl
        decrypt(decrypt_message)
    elif option == 2:
        encrypt_message = str(input("Enter a message to encrypt..."))
        encrypt_key = int(input("key number between 1 and 26"))
        encrypt(encrypt_message, encrypt_key)
    elif option == 3:
        running = False
    else:
        print("1 to decrypt, 2 to encrypt ")