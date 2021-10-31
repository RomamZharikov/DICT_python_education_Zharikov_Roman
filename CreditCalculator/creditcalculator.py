import math

credit = int(input("Enter the loan principal:\n"))
print("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:""")
choice = input()
if choice == "m":
    months = int(input("Enter the monthly payment: \n"))
    repayment = credit // months
    print(f"It will take {repayment} month to repay the loan.")
if choice == "p":
    number = int(input("Enter the number of months: \n"))
    payment = math.ceil(credit / number)
    last_payment = math.ceil(credit - (number - 1) * payment)
    if last_payment != payment:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment}.")
