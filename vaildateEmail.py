#validateEmail

name=input("Enter your name: ")
email=input("Enter your email: ")
if "@" in email and email.endswith(".com"):
    print("Weclome to the platform,", name and "your email is valid.")
else:
    print("Invalid email address. Please try again.")   