amount = float(input("How much money do you get a week? £"))

# Loop
while True:
    save = float(input("How much would you like to save? £"))
    
    if save > amount:
        print("You cannot save more than you get a week.")
    else:
        break

# All the maths
save_amount = save * 52
spend = amount * 52 - save_amount
total = amount * 52

# Output the information
print("Total amount is £" + str(total) + ".")
print("Amount to save is £" + str(save_amount) + ".")
print("Amount to spend is £" + str(spend) + ".")
