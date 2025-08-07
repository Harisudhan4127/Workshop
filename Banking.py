import random

name = input("Ënter the Name : ")
city = input("Ënter the City : ")
age = int(input("Ënter the Age : "))

if 18 < age:
    account = random.randint(10000000,999999999)
    print(f"\nName : {name}\nCity : {city}\nAge : {age}\nBank Account Number : {account}")
else:
    print(f"You are Not eligible!")