import subprocess

option = input("Create cert? (y/n)")

if option == "y":
    subprocess.run([r"C:/Users/Brad/Desktop/Coding/2610Code/Openssl/scripts/create_cert.sh"], shell=True)

subprocess.run([r"C:/Users/Brad/Desktop/Coding/2610Code/Openssl/scripts/verify_cert.sh"], shell=True)

file1 = open("verify.csr", "r") 
print(file1.read())
file1.close()