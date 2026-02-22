# \n  --> This is called 'Escape Sequence' and it is used to go to the next line. 
# 'Akash' , "Akash" , '''Akash'''  => All these 3 type of quotes in string is possible in Python.

str = "This is a string. \nWe are creating in VS Code"
print (str)

#--------------------------------------------------------------------

#Basic Operation
#1 Concatination of string
str1 = "AKASH"
str2 = "KUMAR"
name = str1 + " " + str2
print(name)

#--------------------------------------------------------------------

#2. Length of string
print(len(str1))
print(len(str2))
print(len(name))

#--------------------------------------------------------------------

#3. Indexing on String
# A K A S H _ K U M A R
# 0 1 2 3 4 5 6 7 8 9 10
print(name[0])  #A
print(name[1])  #K
print(name[2])  #A
print(name[3])  #S
print(name[4])  #H
# In string we only can access the element, we can't manipulate the indices.

#--------------------------------------------------------------------

#4. Slicing  --> Accessing parts of a string
# str[starting_idx : ending_idx]  => ending_idx is not included.
# str[ : 4]      =>    same as str[0 : 4]
# str[1 : ]      =>    same as str[1 : len(str)]
print(name[2:5])    #ASH
print(name[:5])    #AKASH
print(name[2:])    #ASH KUMAR

#--------------------------------------------------------------------

# Slicing  -->  Negative Index   (Only in Python)
#  A  P  P  L  E
# -5 -4 -3 -2 -1
fruit = "APPLE"
print(fruit[-3 : -1])   #PL

#------------------------------------------------------------------------

# string functions don't change the original string, it creates copy of the string
str = "i am studying python from youtube playlist"

# 1. str.endswith("ab")         =>   returns true if string ends with the particular substring
print(str.endswith("ist"))

# 2. str.capitalize()           =>   capitalizes 1st char
print(str.capitalize())

# 3. str.replace(old, new)      =>   replaces all old occurences with new
print(str.replace("python", "C++"))

# 4. str.find(word)             =>   retuens 1st index of 1st occurences
print(str.find("from"))

# 5. str.count("ab")            =>   counts the occureneces of substring
print(str.count("i"))

#------------------------------------------------------------------------