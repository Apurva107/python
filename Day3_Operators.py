#OPERATORS

#1 Declare your age as integer variable
age = 25 #int

#2 Declare your height as a float variable
height = 5.6 #float

#3 Declare a variable that store a complex number
a = 3 + 4j #complex

#4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
Base = float(input("Enter base:"))
Height = float(input("Enter height:"))
Area = 0.5 * Base * Height 
print("The area of triangle:",Area)

#5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
perimeter = a + b + c
print("perimeter of triangle:", perimeter)

#6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

print("Rectangle Area:", area_rectangle)
print("Rectangle Perimeter:", perimeter_rectangle)


#7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("enter the radius of circle: "))
Area = 3.14 *r*r
c = 2*3.14*r

print("Area of circle", Area)
print("circumference of circle",c)


#8 Calculate the slope, x-intercept and y-intercept of y = 2x -2


slope = 2            # coefficient of x
y_intercept = -2     # constant term

# x-intercept (set y = 0)
x_intercept = y_intercept / slope * -1

print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)


#9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 , y1 = 2 , 2
x2, y2 = 6 , 10

m = (y2-y1 )/ (x2-x1)
print("Slope",m)

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Distance:", distance)


#Compare the slopes in tasks 8 and 9.
print("The slopes are equal")


#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len("python")
len_dragon = len("dragon")

print(len_python == len_dragon)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

#There is no 'on' in both dragon and python
print(not ('on' in 'dragon' and 'on' in 'python'))

#Find the length of the text python and convert the value to float and convert it to string.
length = len("python")
length_float = float(length)
length_str = str(length_float)

print(length_str)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
print(number % 2 == 0)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

pay = hours * rate
print("Your pay is:", pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years: "))
seconds_in_year = 365 * 24 * 60 * 60
seconds_lived = years * seconds_in_year
print("You have lived approximately", seconds_lived, "seconds.")


