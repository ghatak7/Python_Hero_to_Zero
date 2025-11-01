maxMArks=100
studeentMarks=int(input("Enter the Marks: "))
if studeentMarks>=90 and studeentMarks <= 100:
    print("Grade A")
elif studeentMarks>=75 and studeentMarks<=89:
    print("Grade B")
elif(studeentMarks>=50 and studeentMarks<=74):
    print("Grade C")
else:
    print("Fail")