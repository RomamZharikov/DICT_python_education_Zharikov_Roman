import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--annuity", type=float)
parser.add_argument("--type", type=str)
args = parser.parse_args()


def n(principal, payment, interest):
    i = (interest * 0.01 / 12)
    fraction = (payment / (payment - i * principal))
    result_n = math.ceil(math.log(fraction, i + 1))
    years = result_n / 12
    month = (years - math.floor(years)) * 12
    if math.floor(month) != 0:
        print(f"It will take {math.floor(years)} years and {math.ceil(month)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(years)} years to repay this loan!\n")
    print(f"Overpayment {int(principal * (1 + interest * 0.01 / 0.75) - principal)}")


def a(principal, periods, interest):
    i = (interest * 0.01 / 12)
    num = pow(1 + i, periods)
    result_a = principal * ((i * num) / (num - 1))
    print(f"Your monthly payment = {math.ceil(result_a)}!\n")
    print(f"Overpayment {math.ceil(result_a) * periods - principal}")


def p(payment, periods, interest):
    i = (interest * 0.01 / 12)
    num = pow(1 + i, periods)
    result_p = math.floor(float(payment / ((i * num) / (num - 1))))
    print(f"Your loan principal = {result_p}!\n")
    print(f"Overpayment {payment * periods - result_p}")


def diff(principal, periods, interest):
    i = interest * 0.01 / 12
    month = 0
    result = 0
    steps = list(reversed(range(2, periods + 2)))
    for monthly in steps:
        monthly -= 1
        d = math.ceil(principal / periods) + i * ((principal * monthly) / periods)
        result += d
        month += 1
        print(f"Month {month}: payment is {math.ceil(d)}")
    print(f"Overpayment {math.ceil(result - principal)}")


try:
    if args.type == "annuity":
        if args.payment is not None and args.principal is not None:
            if args.principal > 0 and args.payment > 0 and args.interest > 0:
                n(args.principal, args.payment, args.interest)
            else:
                print("Incorrect parameters")
        elif args.principal is not None and args.periods is not None:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                a(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.payment is not None:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                p(args.payment, args.periods, float(args.interest))
            else:
                print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            diff(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")
