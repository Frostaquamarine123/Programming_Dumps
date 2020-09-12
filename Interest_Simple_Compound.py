def simple_interest(p, t, r):
    # Calculates simple interest
    si = (p * t * r) / 100
    return si


def compound_interest(principle, rate, time):
    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))
    return CI

principal = int(input("Enter the Principal"))
rate = int(input("Enter the rate"))
time = int(input("Enter the time"))
choice = int(input("Enter the choice 1-Simple Interest 2-Compound Interest: "))

if choice == 1:
    si = simple_interest(principal,rate,time)
    print("Simple interest is : " ,si)
else:
    ci = compound_interest(principal,rate,time)
    print("Compound interest is : " ,ci)
