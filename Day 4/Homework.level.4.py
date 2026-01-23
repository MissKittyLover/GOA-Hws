#2) კომენტარების სახით ახსენით თუ რა არის logical operator - ები მოიყვანეთ მაგალითებიც, შემდეგ კი გადახედეთ ქვემოთ მოცემულ კოდს და ახსენით თუ რას გამოიტანს ის

#Logical operators are used to combine conditional statements.
# The three main logical operators are AND, OR, and NOT.
# AND returns True if both statements are true - otherwise it returns False.
# E.g., True and True = True; True and False = False
# OR returs True if at least one statement is true - otherwise it returns False.
#E.g., True or False = True; Flase or Flase = Flase
# NOT reverses the result, returns False if the result is True and True if the result is False.
#E.g., not True = False; not False = True

print(True and True or False or True and True and False)
#The code above will output "True".

print("--------------------------------------------------")

#3) მომხმარებელს შემოატანინეთ თავისი სახელი და ასაკი თქვენი დავალებაა რომ შეამოწმოთ თუ მომხმარებლის მიერ შემოტანილი სახელი უდრის John - ს და მისი ასაკი არის 25 - ის ტოლი მაშინ დაბეჭდეთ მნიშვნელობა 'True' სხვა შემთხვევაში კი 'False'

User_name = input("Enter your name: ")
User_age = int(input("Enter your age: "))

if User_name == "John" and User_age == 25:
    print("True")
else:
    print("False")

print("--------------------------------------------------")

#4)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

average = (num1 + num2 + num3) / 3
print("The average of the three integers is:" , average)

print("--------------------------------------------------")

#5) 

#Sequencing არის ბრძანების თანმიმდევრობა. სადაც კოდი კონკრეტული (მოცემული) თანმიმდევრობით სრულდება.
#Iteration არის ციკლის გამოყენება, რომელიც საშუალებას გვაძლევს გავიმეოროთ კოდის ნაწილი მანამ, სანამ გარკვეული პირობა შესრულდება.
#Selection არის პირობითი ლოგიკა, რომელიც საშუალებას გვაძლევს გავაკეთოთ არჩევანი სხვადასხვა გზებს შორის,
#დამოკიდებული გარკვეული პირობის შესრულებაზე (მაგალითად if-else)

#მათ შორის განსხვავება არის ის, რომ sequencing არის კოდის რიგით შესრულება,
#Iteration არის კოდის ნაწილების გამეორება, ხოლო selection არის გადაწყვეტილებების მიღება პირობითი ლოგიკის საფუძველზე.

#6)

#for loop პითონში გამოიყენება, როცა გინდა, რომ რაღაც მოქმედება განმეორდეს რამდენჯერმე — მაგალითად, როცა სიაში ყველა ელემენტზე გადიხარ.
#E.g., for i in range(5):
    #print(i)
#1. start – საიდან დაიწყოს (ნაგულისხმევად 0).

#2. stop – სად შეწყდეს (არ მოიცავს ამ მნიშვნელობას).

#3. step – რამდენით გადახტეს თითო ბიჯზე (ნაგულისხმევად 1).

#For loop არის კონტროლის სტრუქტურა, რომელიც საშუალებას გვაძლევს გავიმეოროთ კოდის ნაწილი განსაზღვრული რაოდენობის ჯერ.


#7) 

#while ციკლი მუშაობს მანამ, სანამ პირობა ჭეშმარიტია (True).
#ანუ, სანამ პირობა სრულდება — ციკლი ტრიალებს. როცა აღარ სრულდება — ჩერდება.

#for გამოიყენება, როცა იცი რამდენჯერ უნდა განმეორდეს ციკლი.
#while — როცა არ იცი რამდენჯერ, უბრალოდ გინდა, რომ ტრიალოს სანამ პირობა ჭეშმარიტია.

#8) 
Number = int(input("Enter a number to find its factorial: "))
Factorial = 1
if Number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, Number + 1):
        Factorial *= i
    print("The factorial of", Number, "is", Factorial)

print("--------------------------------------------------")
#9)
Score = int(input("Enter your score: "))
if Score >> 90:
    print("A++")
elif Score == 90:
    print("A")
elif Score >= 80:
    print("B")
elif Score >= 70:
    print("C")
elif Score >= 60:
    print("D")
else:
    print("F")

print("--------------------------------------------------")

#10)

Number1 = int(input("Enter the first integer: "))
Number2 = int(input("Enter the second integer: "))
Number3 = int(input("Enter the third integer: "))

if Number1 >= Number2 and Number1 >= Number3:
    print("The largest number is: ", Number1)
if Number2 >= Number1 and Number2 >= Number3:
    print("The largest number is: ", Number2)
if Number3 >= Number1 and Number3 >= Number2:
    print("The largest number is: ", Number3)

print("--------------------------------------------------")


#11) 

for i in range(11):
    print(i)

print("--------------------------------------------------")
#12) 
sum = 0
for i in range(1, 21):
    sum += i
print("The sum of the numbers from 1 to 20 is: ", sum)

print("--------------------------------------------------")


#13) შექმენით ცვლადი სადაც შეინახავთ თქვენს სახელს, გადაუარეთ მას for loop - ის გამოყენებით და დაბეჭდეთ თითოეული სიმბოლო

Name = "Gabriel"
for char in Name:
    print(char)

print("--------------------------------------------------")