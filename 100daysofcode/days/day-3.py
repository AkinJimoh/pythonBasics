#rite a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.
#
# e.g. 86 is even because 86 ÷ 2 = 43
#
# 43 does not have any decimal places. Therefore the division is clean.
#
# e.g. 59 is odd because 59 ÷ 2 = 29.5

# num = int(input("Please enter a number:\n"))
#
# if num % 2 == 0:
#     print(f"The number {num} is an even number")
# else:
#     print(f"The number {num} is an odd number")


# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# w = input("Enter your weight:\n")
# h = input("Enter your height:\n")
# weight = (int(w) / float(h) ** 2)
# bmi = round(weight, 2)
# print(round(bmi, 2))
#
# if bmi <= 18.5:
#     print(f"Your bmi is {bmi} and you are underweight")
# elif bmi <= 25:
#     print(f"Your bmi is {bmi} have a normal weight")
# elif bmi <= 30:
#     print(f"Your bmi is {bmi} are slightly overweight")
# elif bmi <=35:
#     print(f"Your bmi is {bmi} and are obese")
# else:
#     print(f"My God Man!! Your bmi is {bmi} Please lose some weight")


#Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February
# https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf

# year = int(input("Please enter a year:\n"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Is a leap year")
#         else:
#             print("Is not a leap year")
#     else:
#         print("Is a leap year")
# else:
#     print("Is not a leap year")


# Congratulations, you've got a job at Python Pizza.
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15 -- Medium Pizza: $20 -- Large Pizza: $25
# Pepperoni for Small Pizza: +$2 -- Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# bill = 0
# size = input("Please enter a size Pizza.\nChoose s, m or l.\n")
#
# if size == "s":
#     bill =+ 15
# elif size == "m":
#     bill += 20
# else:
#     bill += 25
# pep = input("Do you want pepperoni?\nPlease enter y or n\n")
# if pep == "y":
#     if size == "s":
#         bill +=2
#     else:
#         bill +=3
# che = input("Do you want extra cheese?\nPlease enter y or n\n")
# if che == "y":
#     bill +=1
# print(f"Your final bill is £{bill}")

# print("Welcome to the love calculator\n")
# name1 = input("Please enter your name:\n")
# name2 = input("Please enter your partner's name:\n")
# name3 = (name1 + name2).lower()
# co = 0
# c1 = 0
#
# for i in "true":
#     co += (name3.count(i))
# for i in "love":
#     c1 += (name3.count(i))
# score = int(str(co) + str(c1))
#
# if score < 10 or score > 90:
#     print(f"Your Score is {score} you go together like coke and mentos")
# elif score >= 40 and score <= 50:
#     print(f"Your Score is {score} you are alright together")
# else:
#     print(f"Your Score is {score}")


#https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
# print("Welcome to treasure island:\n")
# c1 = input("Choose left or right:\n").lower()
#
# if c1 == "left":
#     c2 = input("Do you want to swim or wait?\n").lower()
#     if c2 == "wait":
#         c3 = input("What color door do you want to go through?\nPick any colour.\n")
#         if c3 == "red":
#             print("Sorry, you've been burned by fire - Game Over")
#         elif c3 == "blue":
#             print("Sorry, you've been eaten by beasts - Game Over")
#         elif c3 == "yellow":
#             print("Congratulations You Win!!!")
#         else:
#             print("BAD Choice --- Game OVER Mate")
#     else:
#         print("You've been attacked by a trout - Game Over")
# else:
#     print("Sorry you fell into a hole - Game Over")
