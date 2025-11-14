a=input("Enter a word: ")
reverse = ""
for i in range(len(a)-1,-1,-1):
    reverse +=a[i]
b=reverse
if a==b:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")