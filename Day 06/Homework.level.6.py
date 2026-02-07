# 2)

correct_password = "LOLLOLLOL"
attempts = 0

while attempts < 3:
    entered = input("Enter password: ")
    attempts += 1

    if entered == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")

if attempts == 3 and entered != correct_password:
    print("You have reached the maximum number of attempts")

print('------------------------------------------------')

# 3) გადახედეთ მოცემულ კოდს და თქვენით დაფიქრდით თუ რას გამოიტანს ის\

# print(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)
#კოდი გამოიტანს True, რადგან ბოლო ნაწილი არის True და or ოპერატორი მხოლოდ ერთს ითხოვს რომ შედეგი იყოს True

# 4)

#მასივი არის მონაცემთა სტრუქტურა რომელიც საშუალებას გვაძლევს ერთ ცვლადში შევინახოთ მრავალი მნიშვნელობა.
#პითონში მასივს ვუწოდებთ listს და მასში შეგვიძლია შევინახოთ ნებისმიერი მონაცემთა ტიპი.

# 5) 

family_members = ["SIMONA", "JORA", "KUKURA", "JUJUNA"]

for member in family_members:
    print(member)

# 6)

NUMBERZ = [2, 27, 81, 14, 16]
total = 0
for number in NUMBERZ:
    total += number
    print(total)

print('----------------------------------------')

# 7)

#Indexing არის მეთოდი რომლის საშუალებითაც შეგვიძლია მივწვდეთ მასივის ან Stringის კონკრეტულ ელემენტტს მისი პოზიციის მიხედვით.
#რა თქმა უნდა შეგვიძლია გამოვიყენოთ Strungებზე

# 8) 

#Indexingის გამოყენება კარგი პრაქტიკაა რადგან ის საშუალებას გვაძლევს სწრაფად მივწვდეთ კონკრეტულ ელემენტს მასივშ ან სტრინგში,
#რაც ზრდის კოდის ეფექტურობას და წაკითხვის მარტივობას.
#მაგალითად თუ გვსურს მივიღოთ პირველი ან ბოლო ელემენტი მასივიდან, Indexing საშუალებას გვაძლევს ეს მარტივად გავაკეთოთ.

# 9) თქვენით გააკეთეთ indexing - ზე 5-5 მაგალითი და კარგად გაიაზრეთ

MINE = ["A", "B", "C", "D",]
print(MINE[0]) #A
print(MINE[3]) #D

FRUITS = ['apple', 'banana', 'STRAWBERRIES', 'DRAGONfruit']
print(FRUITS[2]) #STRAWBERRIES
print(FRUITS[0]) #apple

CARS = ['BMW', 'AUDI', 'REDBULL(F1)', 'BUGATTI', 'FERRARI']
print(CARS[2]) #REDBULL(F1)
print(CARS[4]) #FERRARI

ANIMALS = ['DOG', 'SPHYNX', 'JAGUAR', 'AYE AYE']
print(ANIMALS[1]) #SPHYNX
print(ANIMALS[3]) #AYE AYE

ARMY_PLANES = ['F22', 'F35', 'SU57', 'J20', 'TEMPEST']
print(ARMY_PLANES[0]) #F22
print(ARMY_PLANES[4]) #TEMPEST

print('----------------------------------------')

# 10) 

FRUITZ = ['RAMBUTAN', 'watermelon', 'PAPAYA', 'kiwi', 'MangoMango', 'Ugli fruit', 'Durian...']
print(FRUITZ[1::2]) #watermelon, kiwi, Ugli fruit
print(FRUITZ[0::2]) #RAMBUTAN, PAPAYA, MangoMango, Durian...

print('-----------------------------------------')

#11) შეგვიძლია თუ არა რომ for loop - ს გადავცეთ 1 - ზე მეტი არგუმენტი, თუ კი ჩამოთვალეთ ისინი და განიხილეთ თითოეული მათგანი, ასევე თქვენთვის გააკეთეთ 2-2 მაგალითი

#