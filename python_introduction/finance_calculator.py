
income = float(input("Enter your monthly income:5000 "))
expenses = float(input("Enter your total monthly expenses:4000 "))
                 
monthly_savings = income - expenses


projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


print("Your monthly savings are $1000.0", monthly_savings)
print("Projected savings after one year, with interest, is: $12600.0", projected_savings)
