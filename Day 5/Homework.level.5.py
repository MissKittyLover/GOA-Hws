#2)

name = "Simon Riley"
for i in name:
    print(i)

print("--------------------------------------------------")
#3)

#for i in name
#print(i)

#The code is missing a colon (:) at the end of the for loop declaration.
#Also, there is no variable or string defined for 'name'.

#4)

#For loop გამოიყენება, როცა ცნობილია რამდენჯერ უნდა გაიმეორო რაღაც. იგი გადის ელემენტებზე (სია, სტრინგი, range და ა.შ.).
#მაგალითი:
for i in range(1, 6):
    print(i)

#ეს დაბეჭდავს 1-დან 5-მდე რიცხვებს.
#იყენებენ როცა:

#გაქვს ელემენტების სია
#გინდა თითოეულზე იგივე ქმედება

#While loop გამოიყენება, როცა წინასწარ არ იცი რამდენჯერ უნდა შესრულდეს კოდი. მუშაობს მანამ, სანამ პირობა True-ა.
#მაგალითი:
i = 1
while i <= 5:
    print(i)
    i += 1

#ის მუშაობს მანამ, სანამ i <= 5.
#იყენებენ როცა:

#მოქმედება უნდა გრძელდებოდეს სანამ რაღაც პირობა შესრულებულია
#(მაგ. სანამ მომხმარებელი არ შეიყვანს სწორ პაროლს)

#განსხვავება:


#for - როცა იცი რამდენჯერ უნდა გაიმეორო
#while - როცა უნდა გაგრძელდეს სანამ პირობა მართალია

print("---------------------------------------------------")
#5) while loop - ის გამოყენებით დაბეჭდეთ რიცხვები 1 დან 10 - ის ჩათვლით

i = 1
while i <= 10:
    print(i)
    i += 1

print("---------------------------------------------------")

#6) გამოიტანეთ რიცხვები 10 - დან 1 - მდე

i = 10
while i >= 1:
    print(i)
    i -= 1

for i in range(10, 0, -1):
    print(i)

print("---------------------------------------------------")


#7) მომხმარებელს შემოატანინეთ თავისი სახელი, თქვენი დავალებაა რომ შეამოწმოთ თუ რამდენი ხმოვანია მასში, შეგიძლიათ მოიძიოთ ინფორმაცია, მინიშნება გამოიყენეთ (if statement, for loop, variables)

vowels = "AEIOUaeiou"
User_name = input("Enter your name: ")
vowel_count = 0
for i in User_name:
    if i in vowels:
        vowel_count += 1
        print(vowel_count)

print("---------------------------------------------------")

#BONUS
#8) შექმენით ერთი ცვლადი სადაც შეინახავთ თქვენთვის სასურველ პაროლს, მომხმარებლის დავალებაა რომ მოცემული პაროლი გამოიცნოს, მომხმარებელს მოსთხოვეთ პაროლის ხელახლა შემოტანა იქამდე სანამ ის არ გამოიცნობს მას, მინიშნება გამოიყენეთ (while loop

correct_password = "IOnlyKneelBeforeMyGodlyFather"
user_input = ""

while user_input != correct_password:
    user_input = input("Please enter the password: ")
    if user_input == correct_password:
        print("Access granted.")
    else:
        print("Incorrect password. Please, try again.")
print("---------------------------------------------------")