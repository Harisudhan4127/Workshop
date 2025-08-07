"""
Purches = int(input("Enter the Purches Amount : "))

if 2000 <= Purches and Purches <= 5000:
    print(f"Your gift voucher is 500 Rs")

elif 5000 <= Purches and  Purches < 10000:
    print(f"Your gift voucher is 1000 Rs")

elif 10000 <= Purches:
    print(f"Your gift voucher is 1500 Rs")

else:
    print(f"Buy more things in Our shope\nYour purches Amount is {Purches}")
"""
Purches = int(input("Enter the Purches Amount : "))

if 2000 <= Purches <= 5000:
    print(f"Your gift voucher is 500 Rs")

elif 5000 <= Purches < 10000:
    print(f"Your gift voucher is 1000 Rs")

elif 10000 <= Purches:
    print(f"Your gift voucher is 1500 Rs")

else:
    print(f"Buy more things in Our shope\nYour purches Amount is {Purches}")