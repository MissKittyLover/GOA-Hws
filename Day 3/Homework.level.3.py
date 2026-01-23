# Level 3

#1)

#a = 5
#b = "3"

#sum = 5 + b
#print(sum)

#correct version...
a = 5
b = 3

sum = a + b
print(sum)

print("--------------------------------------------------")

#2)

#Implicit type conversion

num_int = 10
num_flo = 15.5

total = num_int + num_flo
print("The total is: ", total)

#Explicit type conversion

Num_int = 10
num_str = "5"

num_str_conv = int(num_str)
Total = num_int + num_str_conv

print("The total after type conversion is: ", Total)

print("--------------------------------------------------")

#3)

user_input_flo = input("Enter a number: ")

user_input_flo2 = input("Enter another number: ")

sum = float(user_input_flo) + float(user_input_flo2)

print("The sum of the two numbers is: ", sum)

print("--------------------------------------------------")

#4) 

user_input = int(input("Enter a number: "))
user_input2 = int(input("Enter another number: "))

if user_input %2 == 0 and user_input2 %2 == 0:
    print(user_input + user_input2)
else:
    print("The numbers will not be added as one or both are odd...")

print('--------------------------------------------------')

#5)

User_name = input("Your name is: ")
#Your name is: name
User_surname = input("Your surname is: ")
#Your surname is: surname
User_age = int(input("Your age is: "))
#Your age is: age
User_location_city = input("You live in: ")
#You live in: city
User_location_country = input("The country you live in is: ")
#The country you live in is: country

print(User_name)
print(User_surname)
print(User_age)
print(User_location_city)
print(User_location_country)

print('--------------------------------------------------')

#6) comparation operator

#Equal to (==):

x = 10
y = 20
g = 10
print(x == y)
print(x == 10)
print(x == g)

#Not equal to (!=):

f = 10
l = 20
print(f != l)
print(f != 10)

#Greater than (>):

s = 10
m = 20
print(s > m)
print(m > s)

#Less than (<):

n = 10
m = 20
print(n < m)
print(m < n)

#Greater than or equal to (>=):

v = 10
w = 20
print(v >= w)
print(w >= v)

#Less than or equal to (<=):

o = 10
u = 20
print(o <= u)
print(y <= o)

#Examples with Strings

print('apple' < 'orange')
print('banana' < 'apple')

#Chaining Comparison Operators

p = 5
print(1 < p < 10)
print(10 > p <= 9)
print(5 != p > 4)
print(p < 10 < p*10 == 50)


#7)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("The first number is greater than the second number.")
else:
    print("The second number is greater than or equal to the first number.")

print(num1 + num2)
print(num1 - num2)
print(num2 - num1)
print(num1 * num2)
print(num1 / num2)
print(num2 / num1)
print(num1 % num2)
print(num2 % num1)

print("--------------------------------------------------") 

#8)
My_name = "Mariam"
User_name = input("Enter your name: ")

if User_name == My_name:
    print("We have got the same names!")
else:
    print("Our names do not match :(")

#9) თქვენი სიტყვებით ახსენით თუ რა არის კონკადინაცია და რაში შეიძლება რომ გამოვიყენოთ ჩვენ ის, შემდეგ კი გადახედეთ მოცემულ კოდს და ახსენით თუ რას გამოიტანს ის

#Concatenation is the operation of joining (or adding/linking) two or more strings together.
# It is commonly used to create full sentences or combine different pieces of text.

#print('45' + "45")
#This code will putput '4545' because the numbers are in string format, making them concatenate instead of adding numerically.

#10) მომხმარებელს შემოატნინეთ რაიმე რიცხვი, შეამოწმეთ თუ რიცხვის % 2 ნაშთი უდრის 0 - ს გამოიტანეთ რომ 'The number is even' სხვა შემთხვევაში კი 'The number is odd'

User_number = int(input("Enter a desired number: "))

print(User_number)

if User_number % 2 == 0:
    print("The number is even :)")
else:
    print("The number is odd :(")

print("--------------------------------------------------")

#11)