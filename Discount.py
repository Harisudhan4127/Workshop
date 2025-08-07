cost = int(input("Enter Amount of the Purches : "))
Discount = (cost*10)//100

if 1000 > cost :
    print(f"Your Discount Price is {cost - Discount}")
else:
    print(f"Buy more thing for get Discount\nYour Purches Amount is {cost}")