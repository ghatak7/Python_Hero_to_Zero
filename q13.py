user=input("Enter the username: ")
pas=input("Enter the password: ")

if len(pas)>=8 and "@" in pas:
    print("Username and password are valid.")
else:
    print("Invalid password. Please ensure it is at least 8 characters long and contains '@'.")