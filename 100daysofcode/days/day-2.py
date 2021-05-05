#Write a program that adds the digits in a 2 digit number. e.g.
#If the input was 35, then the output should be 3 + 5 = 8

# num = input("Please enter a 2 digit number:\n")
# one=int(num[0])
# two=int(num[1])
# print(one + two)

# print(3 * (3 + 3) / 3 - 3)

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#Example Input

# weight = 80
#
# height = 1.75
#
# Example Output
#
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
#
# 26

# w = input("Enter your weight:\n")
# h = input("Enter your height:\n")
# bmi = (int(w) / float(h) ** 2)
# print(round(bmi))

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left
#If we live until 90 years old.
# age = int(input("Please enter your current age:\n"))
# days = (90 - age) * 365
# weeks = (90 - age) * 52
# months = (90 - age) * 12
#
# print(f"You have {days} days, {weeks} weeks and {months} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = float(input("Please enter the bill:\n"))
num = int(input("How many people are splitting this:\n"))
total = (bill / num) * 1.12
tot = (total)

print(f"Each person needs to pay £{tot} please, thanks")