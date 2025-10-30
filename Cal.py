user1 = float(input("Enter first number: "))
user = float(input("Enter second number: "))

task=input("Choose an option (one, two, three, four): ")


if task=="one":
 print("The value of ",user1,"+",user,"is:",user+user)
elif task == "two":
 print("The value of ",user1,"-",user,"is:",user-user)
elif task=="three":
 print("The value of ",user1,"/",user,"is:",user/user)
elif task=="four":
 print("The value of ",user1,"*",user,"is:",user*user)
else:
 print("Invalid option selected")

# if task == "one":
#     print("The value of", user1, "+", user, "is:", user1 + user)
# elif task == "two":
#     print("The value of", user1, "-", user, "is:", user1 - user)
# elif task == "three":
#     print("The value of", user1, "/", user, "is:", user1 / user)
# elif task == "four":
#     print("The value of", user1, "*", user, "is:", user1 * user)
# else:
#     print("Invalid option selected")