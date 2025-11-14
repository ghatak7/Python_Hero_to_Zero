# 4️⃣ Find Character Frequency

# Input: "hello" → Output:

# h = 1  
# e = 1  
# l = 2  
# o = 1

user=input("Enter a string: ")
cahr_fre={}
for char in user:
    if char in cahr_fre:
        cahr_fre[char]+=1
    else:
        cahr_fre[char]=1
for char, freq in cahr_fre.items():
    print(f"{char} = {freq}")



