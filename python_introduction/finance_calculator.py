
income_input = input("Enter your monthly income (default is 5000): ")
income = float(income_input) if income_input else 5000


expenses_input = input("Enter your total monthly expenses (default is 4000): ")
expenses = float(expenses_input) if expenses_input else 4000


monthly_savings = income - expenses


projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)