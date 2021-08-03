bawah = 85528
income = float(input("Enter the annual income: "))

if income <= bawah:
    tax = ((income *18) / 100) -556.2
    if tax < 0:
        tax = 0
elif income >= bawah :
    tax = ((income-bawah)*32/100) + 14839.2

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
