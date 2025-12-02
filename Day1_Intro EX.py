# 1.Check the python version you are using

# python --version

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
#addition(+)
#subtraction(-)
#multiplication(*)
#modulus(%)
#division(/)
#exponential(**)
#floor division operator(//)

#Variables

a = 3
b = 4

#addition
print("Addition of numbers",a ,"and", b, "is", a + b)
print("Substraction of numbers",a ,"and", b, "is", a - b)
print("Multiplication of numbers", a , "and", b, "is", a * b)
print("Modulus of numbers", a , "and", b, "is", a % b)
print("Division of numbers", a , "and", b, "is", a / b) #true division
print("Exponential of numbers", a , "and", b, "is", a ** b)
print("Floor Division of numbers", a , "and", b, "is", a // b) #floor division

# 3. Write strings on the python interactive shell. The strings are the following:
#Your name
#Your family name
#Your country
#I am enjoying 30 days of python

print("Anu")
print("P")
print("India")
print("I am enjoying 30 days of python")



# 4. Check the data types of the following data:
#10
#9.8
#3.14
#4 - 4j
#['Asabeneh', 'Python', 'Finland']
#Your name
#Your family name
#Your country

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 -4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Anu"))

# 5. Find an Euclidian distance between (2, 3) and (10, 8)

x1 = 2
x2 = 10

y1 = 3
y2 = 8

#euclidian formula
# d= sqt((x2-x1)2 + (y2-y1)2)

distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5 # **0.5 gives the square root
print("the euclidian distance is:",distance)