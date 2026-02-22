a = 6
b = 3

#Arithmetic Operators (+, -, *, /, %, **)
print("Sum is:", a + b)
print("Difference is:", a - b)
print("Multiply is:", a * b)
print("Division is:", a / b)        #Always gives floating output
print("Modulo is:", a % b)          #Remainder
print("Exponentiation is:", a ** b)          #a^b

print("-----------------------------------------------------")

#Relational / Comparison Operators (==, !=, >, <, >=, <=)
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than equal to:", a >= b)
print("Less than equal to:", a <= b)

print("-----------------------------------------------------")

#Assignment Operators (=, +=, -=, /=, %=, **=)
a = b       # a = 3
a += 2      # a = 5
a -= 3      # a = 2
a *= 2      # a = 4
a /= 1      # a = 4.0
a %= 20     # a = 4.0
a **= 2     # a = 16
print (a)

print("-----------------------------------------------------")

#Logical Operators (not, and, or)
print (not a > b)       # False
print (a>b and a<b)     # Flase
print(a>b or a<b)       # True