# Net Worth Calculator
# What is Net Worth?
# Net Worth = Assets - Liabilities
# Assets - Puts money in your pocket uh bank / bitcoin account uh
# Example - House + Land + Business + All Account Balance + Cash
# Liabilities - Takes money out of your pocket uh bank / bitcoin account uh

assets = int(input("Assets(In $): "))
liabilities = int(input("Liabilities(In $): "))
net_worth = assets - liabilities
print("Your Net Worth is: $ " + str(net_worth))
if assets > liabilities:
    print("Awesome! Keep adding more...")
else:
    print("Oh ho! We need to keep the liabilities under limit, my friend!")
