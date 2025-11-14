user=input("Enter a character: ")
clean=""
for char in user:
 if char.isalnum():
    clean+=char

print("clearner:", clean)
    
    