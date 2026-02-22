# if-elif-else syntax
# if (condition):
#     statement1
# elif (condition):
#     statement2
# else:
#     StatementN

#--------------------------------------------------------------------

#Grade student based on marks
marks = int(input("Enter your marks:"))
if (marks >= 90):
    print("Grade: A")
elif (marks >= 80 and marks < 90):
    print("Grade: B")
elif (marks >= 70 and marks < 80):
    print("Grade: C")
else:
    print("Grade: D")

#--------------------------------------------------------------------

# Nested condiotnals are also possible.