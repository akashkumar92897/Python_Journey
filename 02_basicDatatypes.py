#📦 Variables & Strings in Python
# ------------------------------------------------------------------------
text = 'Text in Python is called a string'
text_2 = "It has to be inside single or double quotes"
text_3 = 'We can use "double quotes" inside single quotes'
text_4 = "And 'vice-versa'" #This is a string.

# Comments
# ------------------------------------------------------------------------
# But we can not right text in python without quotes.
# It will break syntax rule...

#👀 Print Statement
# ------------------------------------------------------------------------
print (text)
print (text_2)
print (text_3)
print (text_4)

#🛑 Special Keywords in python (Don't use it.)
# ------------------------------------------------------------------------
# print
# type
# sum
# filter
# id

# not
# in
# break
# continue
# for
# if
# elif
# else

# int
# str
# bool
# float
# list



#📊 Basic Data-Types in Python
# ------------------------------------------------------------------------
string = "AKASH KUMAR"
num_int = 22
num_float = 99.5
boolean = True #False
none_type = None

# Printing of data-types value
# ------------------------------------------------------------------------
print (string)
print (num_int)
print (num_float)
print (boolean)
print (none_type)

# type(data-type) returns the type of data-type.
# ------------------------------------------------------------------------
print (type(string))
print (type(num_int))
print (type(num_float))
print (type(boolean))
print (type(none_type))


#💪 Simple Exercise
# ------------------------------------------------------------------------
# Not a most efficient way to use variables inside a string
user = 'Akash'
app = 'VS Code'
print('Once upon a time there was a ' + app + ' user named ' + user)
print(user + ' wasted months on soul draining tasks in ' + app)
print('Until one day ' + user + ' said: enough! ')
print('And by accident, he discovered that he could automate his ' + app + ' work with Github Copilot')
print('But ' + user + ' knew nothing about Copilot')
print('And so, ' + user + ' has begun his programming journey with copilot')

# STRING FORMATING
# ------------------------------------------------------------------------
print(f'Once upon a time there was a {app} user named {user}')
print(f' wasted months on soul draining tasks in {app}')
print(f'Until one day {user} said: enough! ')
print(f'And by accident, he discovered that he could automate his {app} work with Github Copilot')
print(f'But {user} knew nothing about Copilot')
print(f'And so, {user} has begun his programming journey with copilot')


# BEFORE Python 3.6.6 - .format()
print ('My name is: {}'.format(user))


# AFTER Python 3.6.6 - f-string or .format()
print (f'My name is: {user}')