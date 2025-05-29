
income = float(input("Enter your monthly income: 500 "))
expenses = float(input("Enter your total monthly expenses: 14 "))
                 
monthly_savings = income - expenses


projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


print("Your monthly savings are $486.0. ", monthly_savings)
print("Projected savings after one year, with interest, is: $6123.6.", projected_savings)
