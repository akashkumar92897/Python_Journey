#1. WAP to check if a number entered by the user is odd or even.
num = int(input("Enter your number: "))
if (num % 2 == 0):
    print(num, "is a even number.")
else:
    print(num, "is a odd number.")

#---------------------------------------------------------------------------

#2. WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    if num1 == num2 == num3:
        print("All 3 numbers are equal.")
    elif num1 == num2:
        print(num1, "&", num2, "are equal & greatest.")
    elif num1 == num3:
        print(num1, "&", num3, "are equal & greatest.")
    else:
        print(num1, "is greatest.")
        
elif num2 >= num1 and num2 >= num3:
    if num2 == num3:
        print(num2, "&", num3, "are equal & greatest.")
    else:
        print(num2, "is greatest.")
        
else:
    print(num3, "is greatest.")

#Short-method
# print("Greatest number is:", max(num1, num2, num3))

#---------------------------------------------------------------------------

#3. WAP to check if a number is a multiple of 7 or not.
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(num, "is a multiple of 7.")
else:
    print(num, "is not a multiple of 7.")
