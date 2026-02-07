# 2) კომენტარების სახით ახსენით თუ რა არის list - ები პითონში, შექმნით ერთი მასივი სადაც შეინხავთ სახელებს თქვენი დავალებაა, რომ მოცემულ მასვის გადაუაროთ for loop - ის გამოყენებით და დაბეჭდოთ თითოეული ელემენტი

#Lists are used to store items in a single variable. They are ordered, changeable, and allow duplicate values.
names = ["KAKHA", "SIMONA", "SAMUELA", "TEMURI", "KOKO"]
for name in names:
    print(name)

# 3) შექმენით მასივი სადაც შეინახავთ ცხოველების სახელებს, თქვენი დავალებაა, რომ მოცემული მასივიდან ამოიღოთ 1 ელემენტი და 1 ელემენტის 2 index - ზე მყოფი ელემენტი

Animals = ["Lynx", "HIPPO", "Monki", "sphynx", "wolf"]
Animals.remove("HIPPO") #Removed 1 element
print(Animals[2]) #Printing element at 2nd index

print('-----------------------------------------')

# 4) შექმენით ერთი მასივი სადაც შეინახავთ ელემენტებს, თქვენი დავალებაა რომ გამოიტანოთ ელემენტები 2 ელემენტიდან 5 ელემენტის ჩათვლით

Elementas = ['Hydrogen', 'Helium', 'Lithium', 'Calcium', 'Beryllium']
print(Elementas[2:6]) #Printing elements from 2nd-5th index

print('------------------------------------------')

# 5) გადახედეთ მოცემულ კოდს კარგად გაიაზრეთ ის, ასევე თითოეული დეტალი ახსენით კომენტარების სახით

real_password = 'Nino1234!' #Correcta passworda
attemps = 3 #Max number of tries

user_attempts = 0 #Initial number of user tries

while attemps > user_attempts: #Loop will continue until the user reaches max attempts
    remaining = attemps - user_attempts #Calculation of remaining attempts
    user_input = input(f'Guess the password again You have {remaining}, Attemp(s) left To Guess the password: ') #Telling the user how many attempts are left
    user_attempts += 1 #Increasing the number of user attempts by 1

    if user_input == real_password: #Checking if the user input matches the real passworda
        print('Congrats you have guessed the correct password!') #Success notification
        break #Exiting the loop if the password is correcta
    else: #In other cases
        print('Wrong please try again later!') #Failure notification
else: #More other cases
     print('You have reached the maximum number of attempts') #Cannot pass.

# 6) მოიძიეთ ინფორმაცია ფუნქციების შესახებ პითონში, უბრალოდ ახსენით კომენტარების სახით რა გგონიათ რა არის ის, რაში შეგვიძლია მისი გამოყენება

#ფუნქცია კოდის ბლოკია. ასრულებს ამოცანას და შეიძლება მიიღოს პარამეტრები და დააბრუნოს შედეგი.
#ფუნქციები საშუალებას გვაძლევენ კოდის ბევრჯერ გამოყენებლად.
#ის შეგვიძლია გამოვიყენოთ კოდის ორგანიზებისათვის, განმეორებადი ამოცანების შესასრულებლად და კოდის წაკითხვისა და შენარჩუნების გასამარტივებლად.


# 7) შექმენით ერთი მასივი, ამ მასივიდან ამოიღეთ მხოლოდ 7 და 9 ელემენტები და გამოიტანეთ ეკრანზე

Mass = ['LOL', 'LMAO', 'IDK', 'BRB', 'GTG', 'TY', 'TBH', 'FYI', 'IDC', 'IDM', 'YW', 'NP']
print(Mass[6]) #7th elementa
print(Mass[8]) #9th element

# 8) მომხმარებელს 5 - ჯერ შემოატანინეთ ტექსტი, თქვენი დავალებაა, რომ შექმნათ ცარიელი მასივი სადაც მომხმარებლის მიერ შემოატნილ მნიშვნელობებს ჩაამატებთ, მოიძიეთ ინფორმაცია append მეთოდზე პითონში

Massi = []
for i in range(5):
    text = input("Enter texta: ")
    Massi.append(text)
print(Massi)

# 9) მოიძიეთ ინფორმაცია მასივის მეთოდებზე, თითოეულზე გააკეთეთ 5-5 მაგალითი და კარგად გაიაზრეთ

# append() - დაამატებს ელემენტს მასივის ბოლოში

Massi = [1, 2, 3]
Massi.append(4)
print(Massi) # [1, 2, 3, 4]

# clear() - წაშლის ყველა ელემენტს
Massi.clear()
print(Massi) # []

# copy() - აბრუნებს მასივის კოპიას
Massi = [1, 2, 3]
New_Massi = Massi.copy()
print(New_Massi) # [1, 2, 3]

# count() - თვლის რომელიც ორივენთურიდანაც
Massi = [1, 'a', 'b', 'a']
print(Massi.count('a')) #2

# extend() -გაფართოებს ორივენთურიდან
Massi = [1, 'a', 'b']
Massi.extend([2, 'c'])
print(Massi) # [1, 'a', 'b', 2, 'c']

# index() -გვეძლევს index-ს
Massi = ['a', 'b', 'c']
print(Massi.index('b')) #1

# insert() -დამატებული ორივენთურიდან
Massi = ['a', 'b', 'c']
Massi.insert(0, 'd')
print(Massi) # ['d', 'a', 'b', 'c']

# pop() -გვეძლევს ორივენთურიდან
Massi = ['a', 'b', 'c']
print(Massi.pop()) # c

# remove() -წაშლის ორივენთურიდან
Massi = ['a', 'b', 'c']
Massi.remove('b')
print(Massi) # ['a', 'c']

# reverse() -გვხმობს ორივენთურიდან
Massi = ['a', 'b', 'c']
Massi.reverse()
print(Massi) # ['c', 'b', 'a']

# sort() -გვხმობს ორივენთურიდან
Massi = [3, 1, 4]
Massi.sort()
print(Massi) # [1, 3, 4]

# 10) კომენტარების სახით ახსენით შეგვიძლია თუ არა რომ მასივში შევინახოთ ბევრი განსხვავებული მონაცემთა ტიპი

#კი, მასივში შეგვიძლია შევინახოთ სხვადასხვა ტიპის მონაცემები.