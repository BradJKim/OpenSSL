import subprocess

def key_extract():
    subprocess.run([r"C:/Users/Brad/Desktop/Coding/2610Code/Openssl/scripts/extract.sh"], shell=True)

def encrypt():
    subprocess.run([r"C:/Users/Brad/Desktop/Coding/2610Code/Openssl/scripts/encrypt.sh"], shell=True)

def decrypt():
    subprocess.run([r"C:/Users/Brad/Desktop/Coding/2610Code/Openssl/scripts/decrypt.sh"], shell=True)


option = input("Select e for encrypt, d for decrypt, or k for key extraction: ")

if option == 'k':
    key_extract()
    print("key extracted")
elif option == 'e':
    # Encryption script
    encrypt()
    print("File Encrypted")
elif option == 'd':
    # Decryption script
    decrypt()
    print("File Decrypted")
else:
    print("Error: Invalid Option") 