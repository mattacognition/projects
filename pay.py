hrs = input("Enter Hours:")
pay = input("Enter Payrate:")
try:
    if float(hrs) > 40:
        ot = float(hrs) - 40
        hrs = 40
    else:
        ot = 0
    earnings = float(hrs) * float(pay) + float(ot) * (float(pay) * 1.5)
    print("Pay:", earnings)
except:
    print("Error, please enter an integer")