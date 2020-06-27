from Macro_Calculator02 import Macro



print("Welcome! Do you want to calculate your macros?")

answer = input("Enter 'yes' to continue, enter 'no' to leave: ")

while True:

    if answer == 'no':
        print("Have a nice day!")
        break

    gender = input("Enter your Gender (Male/Female): ").lower()
    age = int(input("Enter your age: "))
    height = int(input("Enter yout height (cm): "))
    weight = int(input("Enter your weight (kg): "))
    active = input("Active Level: ").title()

    data = Macro(gender, age, height, weight, active)

    calculate = data.calculate()

    result = data.show_result()

    reply = input("Do you want to try again (y/n): ")

    if reply =='n':
        break
