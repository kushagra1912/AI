def compound_Interest(principal, rate, time):
    interest = principal * (1 + rate) ** time
    print("Compound Interest: {}".format(interest))