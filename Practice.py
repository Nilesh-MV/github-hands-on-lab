# a = "Pro Player"
# print(a[0:3:1])
# b = "Noob Player"
# print(b[0:4:1])

# a = "123456789"
# a = int(a)
# print(type(a))

# name = "Nilesh"
# age = 21
# print(f"Hello My name is {name} and I am {age} years old.")

# Name = input("Enter your Name: ")
# Age = int(input("Enter your Age: "))
# print(f"Hello My Name is {Name} and I am {Age} Years Old.")
# print(type(Age))

# a = 100
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)
# print(a % b)

# # # # #Assignment Operators
# a = 9

# # # #Compound Assignment Operators
# a=9
# a+=1
# a-=1
# a*=1
# a/=1
# a//=1
# a**=1
# a%=1
# print(a)

# #Logical Operators
# print(5>3 and 9>7)
# print(10<20 or 5>10)
# print(not(10<20 or 5>10))

#if else staements
# a = 100
# if a>10:
#     print("A is Greater than 10")
# else:
#     print("A is Less than 10")

# money = int(input("Please give me Money: "))
# if money == 100:
#     print("I will Buy Corneto Ice Cream.")
# else:
#     print("I will Buy Kulfi Ice Cream.")

# money = int(input("Please give me Money: "))
# if money == 30:
#     print("I will Buy Corneto Ice Cream.")
# elif money == 50:
#     print("I will Buy Kulfi Ice Cream.")
# else:
#     print("I will Buy Magnum Ice Cream.")

#Q1. Accept two number and print the greatest number.
# first_number = int(input("Enter Your First Number: "))
# second_number = int(input("Enter Your Second Number: "))
# if first_number > second_number :
#     print(f"{first_number} is Greater than {second_number}.")
# elif second_number > first_number:
#     print(f"{second_number} is Greater than {first_number}.")
# else:
#     print("Both Entered Numbers are equal.")

#Q2. Accept two gender from user and print respective greetings acc to gender.
# gender = input("Enter your Gender as Character ( M / F ):")
# if gender == "M" or gender == "m":
#     print("Good Mornig Sir...")
# elif gender == "F" or gender == "f":
#     print("Good Morning Ma'am...")
# else:
#     print("Unidentified Gender...")

#Q3. Accept an integer and check whether it is even or odd.
# num = int(input("Enter Your Number: "))
# if num%2 == 0:
#     print("The given number is Even Number.")
# else:
#     print("The given number is Odd Number.")

# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age: "))
# if age >= 18:
#     print(f"Hello {name}You are eligible for voting.")
# else:
#     years_left = 18 - age
#     print(f"Hello {name}You are not eligible for voting. But you can vote after {years_left} years.")

#Checking the entered Year is a Leap Year or not.
# year = int(input("Enter Year: "))

# Combined logic into a single, clean expression
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap Year.")
# else:
#     print(f"{year} is not a Leap Year.")

#Condition(if-elif) Ladder.
# degree = int(input("Enter Degree: "))

# if degree < 0:
#     print("The Temperature is Freezing Cold.")
# elif 0 <= degree <= 10:
#     print("The Temperature is Very Cold.")
# elif 10 <= degree <= 20:
#     print("The Temperature is Cold.")
# elif 20 <= degree <= 30:
#     print("The Temperature is Pleasant.")
# elif 30 <= degree <= 40:
#     print("The Temperature is Hot.")
# elif degree > 40:
#     print("The Temperature is Very Hot.")

#For Loop.
#Printing Table of any number.
# n = int(input("Enter the number fpr printing table: "))
# for i in range(1,11):
#  print(f"{i} * {n} = {i*n}")

#Printing characters using Range.
# a = "Nilesh plays BGMI Game and He is a Pro Player. "
# for i in range(len(a)):
#     print(a[i])

#Break and Continue.
# for i in range(1,20):
#     if i == 15:
#         break
#     print(i)

# for i in range(1,20):
#     if i == 15:
#         continue
#     print(i)

#Accept an integer and print statement n times.
# n = int(input("Enter the number for printing statements repeatedly: "))
# for i in range(n):
#     print("Hello Pro player.")

#Print natural number upto n.
# n = int(input("Enter the Number: "))
# for i in range(1,n+1):
#     print(i)

#Reverse for loop.
# n = int(input("Enter the Number: "))
# for i in range(n,0,-1):
#     print(i)

#Sum upto n terms.
# n = int(input("Enter the number:"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"Sum of the given numbers is {sum}.")

#Print Factorial of a number.
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"Factorial of the given numbers is {fact}.")

#Print sum of all even and odd numbers seperately.
# n = int(input("Enter the number: "))
# even_sum = 0
# odd_sum = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print(f"Sum of all Even Numbers is {even_sum}.")
# print(f"Sum of all Odd Numbers is {odd_sum}.")

#Print factors of all numbers.
# n = int(input("Enter the number: "))
# print(f"The Factors of {n} are: ")
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)

#Take number from user and verify it is perfect number or not.
# n = int(input("Enter the number: "))
# perfect = 0
# print(f"The Factors of {n} are: ")
# for i in range(1,n):
#     if n%i == 0:
#         perfect += i
#         print(i)
# if perfect == n:
#     print(f"{n} is an Perfect Number.")
# else:
#     print(f"{n} is Not an Perfect Number.")

#CHeck Whether given number is prime or not.
# n = int(input("Enter the number: "))

# prime = True

# for i in range(2, n):
#     if n % i == 0:
#         prime = False
#         break

# if prime:
#     print(f"{n} is a Prime Number.")
# else:
#     print(f"{n} is not a Prime Number.")

#Reverse a string.
# s = input("Enter the string to be reversed: ")
# rev = ""

# for i in range(len(s)-1,-1,-1):
#     rev += s[i]

# print(f"The reverse of {s} is {rev}.")

#Chech given string is palindrome or not.
# s = input("Enter the string to be checked it is palindrome or not: ")
# pal = ""

# for i in range(len(s)-1,-1,-1):
#     pal += s[i]

# if s == pal:
#     print(f"{s} is Palindrome.")
# else:
#     print(f"{s} is not Palindrome.")

#Count every alphabet number and special char given by user.
# s = input("Enter the input to be count by category: ")
# char = 0
# num = 0
# spchar = 0

# for i in s:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         num += 1
#     else:
#         spchar += 1

# print(f"Sum of Alpabets are {char}.")
# print(f"Sum of Digits are {num}.")
# print(f"Sum of Special Characters are {spchar}.")

#While Loop.
#Print every digit in next line.
# num = int(input("Enter the number to be seperated: "))

# while num > 0:
#     print(num % 10)
#     num = num // 10

#Accept a num and print its reverse.
# num = int(input("Enter your number to be reversed: "))
# rev = 0

# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10

# print(rev)

#Check given num is Palindrome or not.
# num = int(input("Enter your number to be reversed: "))
# original = num
# rev = 0

# while num > 0:
#     rev = rev * 10 + num % 10
#     num = num // 10

# if original == rev:
#     print(f"{original} is Palindrome.")
# else:
#     print(f"{original} is not Palindrome.")

#Random Number Gusser Game.
# import random
# num = random.randint(1,10)
# tries = 0

# while True:
#     guess = int(input("Enter a number between 1 to 10: "))
#     if guess == num:
#         tries += 1
#         print(f"You are right you guessed the number in {tries} tries.")
#         break
#     elif guess > num:
#         tries += 1
#         print("Go a little lower.")
#     elif guess < num:
#         tries += 1
#         print("Go a little higher.")
#     else:
#         tries += 1
#         print("You are wrong.")

#Functions.
# def palindrome(str):
#     rev = ""
#     for i in range(len(str)-1,-1,-1):
#         rev += str[i]
#     if rev == str:
#         print(f"{str} is a Palindrome.")
#     else:
#         print(f"{str} is not a Palindrome.")

# palindrome("Nilesh")
# palindrome("MOM")
# palindrome("Rotator")

