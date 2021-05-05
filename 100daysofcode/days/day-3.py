#rite a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.
#
# e.g. 86 is even because 86 ÷ 2 = 43
#
# 43 does not have any decimal places. Therefore the division is clean.
#
# e.g. 59 is odd because 59 ÷ 2 = 29.5

num = int(input("Please enter a number:\n"))

if num % 2 == 0:
    print(f"The number {num} is an even number")
else:
    print(f"The number {num} is an odd number")
