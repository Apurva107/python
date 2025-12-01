# DATA TYPES
# Python has multiple built-in data types to represent different kinds of values.
# Common types include integers, floats, strings, booleans, and NoneType.

# 1. Numbers - int, float, complex
# Integers - whole numbers
age = 25 #int data type
score = 100 
a = 150


# Floats - numbers with decimals
price = 19.99 #float
temperature = 98.6
c = 30.3

# Complex - numbers with real and imaginary parts (advanced math)
z = 2 + 3j  # j represents the imaginary unit in Python

# 2. String - str represents text or sequence of characters.
#Use single ' or double " quotes
#Triple quotes """ for multi-line text
b = "Hello"   # str (double quotes)
d = 'Hi'      # str (single quotes)
e = "1234"    # str (looks like a number, but it's a string)

# 3. Boolean - bool
#Booleans represent True or False values - essential for making decisions in code.
#They are case sensitive, they must start with capital letter.

f = True
g = False

# 4. None Type 
# none represents “nothing” or “no value”.
k = None
i = ""    # str - empty string
j = " "   # str - contains a single space

#Using type() to Check Data Types and Typecasting
#
text   = "hi"
number = 10

print(type(text))    # <class 'str'>
print(type(number))  # <class 'int'>

# A number can be converted into string and vice versa
str(31) #"31" integer to string conversion.
int("32") # 32 string to integer