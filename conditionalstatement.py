#Can apply for dl or not?
age = int(input("Enter the age : "))
if (age >= 18):
    print("You can apply for a dl.")
else:
    print("You cannot apply for a dl.")

    #for grading
mark = input("Enter the marks : ")
marks = int(mark)
if (marks >= 90):
    print("Grade A")
elif (marks >= 80):
    print("Grade B")
elif (marks >= 70):
    print("Grade C")
elif (marks >= 60): 
    print("Grade D")
else:
    print("Fail")    