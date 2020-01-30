# Divide and Conquer to Multiply Money
# They say "Dont put all your eggs in a single basket"
# So divide your wealth and diversify your portfolio
# Watch how it multiplies and alter your course if needed

# How long does it take to double your wealth
amount = int(input("Enter the amount you want to double: "))
annual_returns = int(input("Average Annual Returns: "))
double = amount * 2
years = 72 / annual_returns
if annual_returns >= 30:
    print("It will take just " + str(years) + " years to double. The final amount equals " + str(double) +
          "\nThat's mind boggling! Partners?")
else:
    print("It will take " + str(years) + " years to double. The final amount equals " + str(double))
#    diversify = input(("Do you want to diversify your portfolio? (y/n): "))
#    if diversify == 'Y' or 'y':
#        number = int(input("Into how many slices: "))
#        portfolio = int(amount / number)
#        print(portfolio)
#    else:
#        print("Thank you!")
