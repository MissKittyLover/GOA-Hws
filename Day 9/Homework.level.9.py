# 2) კომენტარების სახით ახსენით თუ რა არის default parameters - რაში გამოვიყენებთ ჩვენ მას, რას აკეთებს return

# Default parameters არის ფუნქციის პარამეტრები რომლებსაც აქვთ წინასწარ განსაზღვრული მნიშვნელობები.
# თუ ფუნქცია გამოიძახება და არგუმენტი არ გადაეცემა ამ პარამეტრს, მაშინ გამოიყენება default მნიშვნელობა.
# Return არის ფუნქციის ნაწილი რომელიც განსაზღვრავს რა მნიშვნელობა უნდა დაუბრუნდეს ფუნქციის შესრულების შემდეგ.
# ჩვენ ვიყენებთ default parameters რათა გავამარტივოთ ფუნქციის გამოძახება და შევამციროთ საჭირო არგუმენტის რაოდენობა.

# 3) შექმენით ფუნქცია სახელად which_is_greater რომელიც იღებს ორ არგუმენტს, თქვენი დავალებაა, რომ შეამოწმოთ თუ რომელია ამ ორი რიცხვიდან დიდი, თუ პირველი რიცხვი მეორეზე მეტია გამოიტანეთ message - The first number is greater than the second number, თუ მეორე მეტია პირველზე გამოიტანეთ The second number is greater than the first number სხვა შემთხვევაში კი they are equal to each othe

num1 = 7
num2 = 7.74

def which_is_greater(num1, num2):
    if num1 > num2:
        return "The first number is greater than the second number."
    elif num2 > num1:
        return "The second number is greater than the first number."
    else:
        return "They are equal to each other."
    
print(which_is_greater(num1, num2))

print('----------------------------------------')
# 4) შექმენით ფუნქცია სახელად sum რომელიც არგუმენტად იღებს მასივს, თქვენი დავალებაა, რომ გამოიტანოთ ამ მასივში არსებული რიცხვების ჯამი

def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
num_list = [10, 21, 43, 9, 5]
print(f'The sum of the numbers in the list is: {sum(num_list)}')

print('----------------------------------------')

# 5) შექმენით ფუნქცია სახელად count_vowels რომელიც იღებს ერთ არგუმენტს, თქვენი დავალებაა, რომ დაითვალოთ გადმოცემული ტექსტის ხმოვნების რაოდენობა

def count_vowels(text):
    vowels = "AEIOUaeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

input_text = "Hello pEoPLe. Buy me a MOTORBIKE or an F1 PLANE :)"
print(f'The number of vowels in the text is: {count_vowels(input_text)}')

print('----------------------------------------')

# 6) შექმენით ფუნქცია სახელად is_palindrome რომელიც იღებს string - ს, თქვენი დავალებაა, რომ შეამოწმოთ არის თუ არა გადმოცემული string - ი palindrome, თუ არის მაშინ გამოიტანეთ მნიშვნელობა 'This text is palindrome' სხვა შემთხვევაში კი 'This text is not a palindrome'

# palindrome meaning ---> a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

def is_palindrome(text):
    cleaned_text = text.replace (" ", "").lower() #removing spaces and converting to lowercase
    if cleaned_text == cleaned_text[::-1]:
        return 'This text is palindrome.'
    else:
        return 'This text is not a palindrome.'
input_text = "A man"
print(is_palindrome(input_text))

print('-----------------------------------------')

# 7) შექმენით ფუნქცია სახელად is_uppercase რომელიც იღებს string - ს, თქვენი დავალებაა, რომ შეამოწმოთ არის თუ არა მოცემული ტექსტი მაღალ რეგისტრში თუ არის დააბრუნეთ True სხვა შემთხვევაში False

def is_uppercase(text):
    return text.isupper()
input_text = "HELLO SUCKERS"
print(is_uppercase(input_text))

print('----------------------------------------')

# 8) გააკეთეთ list, string methods - ებზე რამოდენიმე მაგალითი

#LIST
fruits = ['apple, pomegranate, honeydew, skuash']
fruits.append('date') # AddINg 'date' to the list
print(fruits)
fruits.sort() #SoRTinG the list in AlPhaBeTiCaL oRdeR
print(fruits)
print(' - - - - - - - - - - - - ')
#STRING
greeting = "Hello, weaklings :p"
print(greeting.lower()) #ConVerTinG to lowercase
print(greeting.replace("weaklings", "pathetic beings")) #RePLacINg a word
print(greeting.split(",")) #SpLiTtinG the string into a list
print(greeting.find("weaklings")) #FiNDiNg the imdex of a substring

print('----------------------------------------')

# BONUS
# 9) შექმენით ფუნქცია სახელად remove_duplicates რომელიც არგუმენტად იღებს მასივს, თქვენი დავალებაა, რომ მოცემული მასივიდან ამოიღოთ ყველა ისეთი ელემენტი რომელიც მეორდება ერთზე მეტჯერ

def remove_duplicates(input_list):
    unique_list = []
    for i in input_list:
        if input_list.count(i) == 1:
            unique_list.append(i)
        return unique_list
sample_list = [1, 3, 21, 3, 7, 6, 7, 66, 1, 9, 43]
print(f'List after removing duplicates: {remove_duplicates(sample_list)}')