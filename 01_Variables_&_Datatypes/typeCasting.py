#Explicit Conversion  =>  Also called Type Casting and forced by the programmer
x = 50.75
print (int(x))      #50


#Implicit Conversion  =>  Also known as coercion and done automatically during run-time by python
num1 = 10
num2 = 20.45
sum = num1 + num2
print (sum)     # 30.45
print(type(sum))       # float