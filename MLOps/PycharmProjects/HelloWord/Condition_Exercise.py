priceofhouse = 1000000.0

has_good_credit = True

if has_good_credit:
    down_payment = priceofhouse * 10/100
else:
    down_payment = priceofhouse * 20/100

print (down_payment)
print(f"Down Payment: ${down_payment}")

has_high_income = False

if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Denied for loan")

has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for employment")
else:
    print("Not eligible for employment")