import random

response = input("Press 'Y' to roll the dice or Press 'N' to exit: ")
if (response == "N" or response == "n" or response == "no" or response == "No" or response == "NO"):
        print("Thank You! Hope you enjoyed!")

while (response == "Y" or response == "y" or response == "yes" or response == "Yes" or response == "YES"):
    number = random.randint(1,6) 
    if (number == 1):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""|     |""\n""|  ●  |""\n""|     |""\n""|_____|")
    elif (number == 2):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""| ●   |""\n""|     |""\n""|   ● |""\n""|_____|")
    elif (number == 3):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""|   ● |""\n""|  ●  |""\n""| ●   |""\n""|_____|")
    elif (number == 4):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""| ● ● |""\n""|     |""\n""| ● ● |""\n""|_____|")
    elif (number == 5):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""| ● ● |""\n""|  ●  |""\n""| ● ● |""\n""|_____|")
    elif (number == 6):
        print("\n""After Rolling the Dice, the value is:-""\n""|‾‾‾‾‾|""\n""| ● ● |""\n""| ● ● |""\n""| ● ● |""\n""|_____|")

    response = input("Press 'Y' to roll the dice once again or Press 'N' to exit: ")
    if (response == "N" or response == "n" or response == "no" or response == "No" or response == "NO"):
        print("Thank You! Hope you enjoyed!")