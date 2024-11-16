import math

def add(num1,num2):
    addition = num1+num2
    return addition

def sub(num1,num2):
    substraction = num1-num2
    return substraction
def multi(num1,num2):
    multipli= num1*num2
    return multipli
def div(num1,num2):
    division = num1/num2
    return division
def pow(num1,num2):
    power = math.pow(num1,num2)
    return power

while True:
    opp = input("Enter the opperator:")
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if opp =='+':
        print("The Answer is",add(num1,num2))
    if opp =='-':
        print("The Answer is",sub(num1,num2))
    if opp =='*':
        print("The Answer is",multi(num1,num2))
    if opp =='/':
        print("The Answer is",div(num1,num2))
    if opp =='**':
        print("The Answer is ",pow(num1,num2))

    choice=input("Enter the choice: ")
    if choice=="y":
        continue
    elif choice=="n":
        break

