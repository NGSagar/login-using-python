import time

username = "Ronaldo"
password = "secretpassword"

username_input = input("Username: ")
password_input = input("Password: ")

if username_input == username and password_input == password:
    print("Access granted")
    print("Please wait..")
    time.sleep(5)
    print("Ok.. Loading..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    print("All right You've security clearance. Pulling up the secret mainframe.")

elif username_input != username and password_input == password:
    print("Username Incorrect")
elif username_input == username and password_input != password:
    print("Password Incorrect")

else:
    print("You might wanna check out both fields....!!!")

    