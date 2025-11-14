#reverse.py

a=input("Enter a word: ")
reverse = ""
for i in range(len(a)-1,-1,-1):
    reverse += a[i]
print("The reversed word is:", reverse)