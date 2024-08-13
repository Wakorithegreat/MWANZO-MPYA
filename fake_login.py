import time
username = "Thor"
password = "Thestrongestavenger"
username_input = input("Enter the username: ")
password_input = input("Enter the passphrase:")

if username_input == username and password_input == password:
    print("Access granted!")
    print("Please wait")
    time.sleep(5)
    print("Ok ... loading ...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    print("Your have connected securely!")
elif username_input == username and password_input != password:
    print("Incorrect Passphrase!")
elif username_input != username and password_input == password:
    print("Forgot you're username?")
else:
    print("Unaguess tu!")