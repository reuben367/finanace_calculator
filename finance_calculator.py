# code to calculate return on simple and compound investments and monthly repayments on a home loan

import math

# provide users with choice of investment or bond calculator

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

choice_list = ["investment", "bond"]
# Check user input is valid
while True:
    finance_choice = input("Enter either 'investment' or 'bond' from the above to proceed: ")
    finance_choice = finance_choice.lower()
    finance_choice = finance_choice.strip()
    if finance_choice in choice_list:
        break

while True:    
    # if user choses investment collect data and calculate simple or compound depending on user input
    if finance_choice == "investment":
        deposit = int(input("Enter amount to be invested in £: "))
        rate = float(input("Enter interest rate as a %: "))
        time = int(input("Enter investment time in years: "))
        interest = input("Enter interest type (simple or compound): ")
        
        while True:
            if interest == "simple":
                total_return = deposit * (1 + (rate / 100) * time)
                print(f"Total return is £{int(total_return)}")
                break
            if interest == "compound":
                total_return = int(deposit * math.pow((1 + rate/100), time))
                print(f"Total return is £{int(total_return)}")
                break
            interest = input("You need to enter interest type, try again (simple or compound): ")
        break

    # if user choses bond collect data and calculate monthly repayments
    if finance_choice == "bond":
        current_value = int(input("Enter current house value in £: "))
        rate2 = float(input("Enter interest rate as a %: "))
        time2 = int(input("Enter repayment period in months: "))
        monthly_repayment = ((rate2/1200) * current_value) / (1 - (1 + (rate2/1200))**-time2)
        print(f"Monthly repayments are £{int(monthly_repayment)}")
        break
