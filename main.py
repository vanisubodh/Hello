from getpass import getpass

password = getpass()
if(password != ""):
    print("Received a password")
else:
    print("Did not receive a password")
     