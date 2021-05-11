#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#There are a total of 7 heights in student_heights
#1146 ÷ 7 = 163.71428571428572
#Average height rounded to the nearest whole number = 164
#Important You should not use the sum() or len() functions in your answer.
# Try to replicate their functionality using what you have learnt about for loops.

# student_heights = input("Input a list of student heights:\n").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# new = 0
# for i in student_heights:
#     new += i
# print(new)
#
# new1 = 0
# for i in student_heights:
#     new1 += 1
# print(new1)
#
# avg = (new / new1)
# print(round(avg))

#You are going to write a program that calculates the highest score from a List of scores.
#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#Important you are not allowed to use the max or min functions.
#The output words must match the example. i.e
#The highest score in the class is: x

# student_scores = input("Input a list of student scores:\n ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# hgh = 0
# for i in student_scores:
#     if i > hgh:
#         hgh = i
# print(f"The highest score in the class is {hgh}")

#You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
#Thus, the first even number would be 2 and the last one is 100:

# cc = 0
# for i in range(2, 101, 2):
#     cc += i
# print(cc)

#or
# cc = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         cc += i
# print(cc)

#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#         continue
#     elif i % 3 == 0:
#         print("Fizz")
#         continue
#     elif i % 5 == 0:
#         print("Buzz")
#         continue
#     print(i)

#or

# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# for i in range(0, nr_letters):
#     a = random.choice(letters)
#     for i in range(0, nr_symbols):
#         b = random.choice(symbols)
#         for i in range(0, nr_numbers):
#             c = random.choice(numbers)
#     d = (f"{a}{b}{c}")
#     print(d, end = '')

password = ""
for i in range(0, nr_letters):
    password += random.choice(letters)
for i in range(0, nr_symbols):
    password += random.choice(symbols)
for i in range(0, nr_numbers):
    password += random.choice(numbers)
a = ''.join(random.sample(password,len(password)))
print(f"Your password is {a}")



