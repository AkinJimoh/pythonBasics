#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#There are many ways of doing this.
#But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1.
#Then use that number to print out Heads or Tails.
#e.g.
#1 means Heads
#0 means Tails

# import random
# print("Welcome to the virtual coin toss program:\n")
# a = random.randint(0,1)
# if a == 0:
#     print("Heads")
# else:
<<<<<<< HEAD
#     print("Tails")

#You are going to write a program which will select a random name from a list of names.
#The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function

# aj = input("Please provide a number of names separated by a comma:\n")
# op = aj.split(" ")
# rd = random.choice(op)
# s = rd.replace(',', '')
# print(f"{s} is going to pay the bill today")

# import random
# names_string = input("Give me everybody's names, separated by a comma\n")
# names = names_string.split(", ")
# num = len(names)
# rd = (random.randint(0, num -1 ))
# name = (names[rd])
# print(f"{name} is going to buy the meal today")

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?\n")
# p1 = int(position[0]) - 1
# p2 = int(position[1]) - 1
#
# map[p1][p2] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# import random
#
# num = int(input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for scissors.\n"))
# aj = [rock, paper, scissors]
# cc = random.randint(0,2)
# cc1 = aj[cc]
#
# if num == 2 and cc == 0:
#     print(aj[num])
#     print(f"Computer chose\n {cc1}\n You Lose" )
# elif num == 1 and cc == 2:
#     print(aj[num])
#     print(f"Computer chose\n {cc1}\n You Lose")
# elif num == 1 and cc == 0:
#     print(aj[num])
#     print(f"Computer chose\n {cc1}\n You Win")
# else:
#     print("Draw")
=======
#     print("Tails")
>>>>>>> 05487de (Added day-4 files)
