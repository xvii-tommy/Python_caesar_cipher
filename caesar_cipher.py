alphabet = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n","o","p",
            "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

secret_message = []


def decrypt(text):
    for key in range(0, 26):
        for letter in text:
            for i in range(len(alphabet)):
                if letter == alphabet[i]:
                    secret_message.append(alphabet[(i + key) % len(alphabet)])
        print(key)
        print(secret_message)
        secret_message.clear()


def encrypt(text, key):
    for letter in text:
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                secret_message.append(alphabet[(i + key) % len(alphabet)])
        print(secret_message)
        secret_message.clear()


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