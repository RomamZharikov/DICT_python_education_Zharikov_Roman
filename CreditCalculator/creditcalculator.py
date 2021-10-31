import math


def n():
    credit = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))
    i = (loan_interest * 0.01 / 12)
    fraction = (monthly_payment / (monthly_payment - i * credit))
    result_n = math.ceil(math.log(fraction, i+1))
    years = result_n / 12
    month = (years - math.floor(years)) * 12
    if math.floor(years) != 0:
        print(f"It will take {math.floor(years)} years and {math.ceil(month)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(years)} years to repay this loan!\n")


def a():
    credit = int(input("Enter the loan principal:\n"))
    period = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))
    i = (loan_interest * 0.01 / 12)
    num = pow(1 + i, period)
    result_a = credit * ((i * num) / (num - 1))
    print(f"Your monthly payment = {math.ceil(result_a)}!\n")


def p():
    annuity = float(input("Enter the annuity payment:\n"))
    period = int(input("Enter the number of periods:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))
    i = (loan_interest * 0.01 / 12)
    num = pow(1 + i, period)
    result_p = annuity / ((i * num) / (num - 1))
    print(f"Your loan principal = {math.floor(result_p)}!\n")


while True:
    choice = input(f"""What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:\n""")
    if choice == "n":
        n()
    if choice == "a":
        a()
    if choice == "p":
        p()
