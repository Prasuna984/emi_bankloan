def calculate_emi(principal, annual_interest_rate, time_in_years):
    rate_per_month = (annual_interest_rate / 100) / 12  # Convert annual rate to monthly rate
    total_months = time_in_years * 12  # Total number of months

    # EMI formula
    emi = (principal * rate_per_month * (1 + rate_per_month) ** total_months) / \
          ((1 + rate_per_month) ** total_months - 1)
    
    return emi


print("WELCOME TO HAHA BANK")
print("Enter the information needed for your HOME LOAN")

# Taking input from user
principal = float(input("Enter principal amount: "))  
annual_interest_rate = float(input("Enter annual interest rate (in percentage): "))  
loan_duration_years = int(input("Enter loan duration in years: ")) 

# Calculate EMI
monthly_emi = calculate_emi(principal, annual_interest_rate, loan_duration_years)

# Display result
print(f"Your monthly EMI is: {monthly_emi:.2f}")
print("THANK YOU FOR TAKING A LOAN AT OUR BANK")
print("VISIT AGAIN")
