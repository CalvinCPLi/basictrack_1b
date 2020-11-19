#2.5
principle = int(input("What is your initial investment?"))
interest_rate = float(input("What is the current interest rate per year?"))
interest_rate_percent = interest_rate / 100
compound_period = int(input("How many times is it compounded per year?"))
years = int(input("For how many years is it compounding?"))
final_amount = principle*((1 + (interest_rate_percent / compound_period)) ** (years * compound_period))
print(final_amount)