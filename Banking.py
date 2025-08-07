import random

def bank():
        balance = 10000
        while 1:
            print("=========== Bank system ===========")
            option = int(input("1. Credit\n2. Debit\n3. Balance\n4. Exit\nEnter The Option: "))
            if option ==1:
                credits = int(input("Enter Credit Amount : "))
                balance = balance + credits
                print(f"Your accoun balance is {balance}")
            elif option ==2:
                Debit = int(input("Enter Debits Amount : "))
                balance = balance - Debit
                print(f"Your accoun balance is {balance}")
            elif option ==3:
                print(f"Your accoun balance is {balance}")
            elif option ==4:
                print("You for using Our Bank System")
                break
            else:
                print("Your Entered Invalid Option")

name = input("Ënter the Name : ")
city = input("Ënter the City : ")
age = int(input("Ënter the Age : "))

if 18 < age:
    account = random.randint(10000000,999999999)
    print(f"\nName : {name}\nCity : {city}\nAge : {age}\nBank Account Number : {account}")
else:
    print(f"You are Not eligible!")
    exit()
user = account
if account == user:
    print("")
else:
    print("Account Number is Incorrect!")
bank()
    