#vowel.py

user=input("Enter a sentence: ")
vowels="aeiouAEIOU"
vowels_count=0
consononets_count=0

for char in user:
    if char.isalpha():
     if char in vowels:
        vowels_count+=1
     else:
        consononets_count+=1
print("Vowels:",vowels_count)
print("consononets:",consononets_count)

