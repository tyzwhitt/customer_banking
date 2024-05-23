# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input("\nEnter your savings account balance ")
    #savings_balance = float(savings_balance)

    savings_interest = input("Enter your interest rate ")
    #savings_interest = float(savings_interest)

    savings_maturity = input("Enter in the number of months ")
    #savings_maturity = int(savings_maturity)
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(float(savings_balance), float(savings_interest), int(savings_maturity))

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nSavings Balance: ${updated_savings_balance: .2f}\nInterest Earned: ${interest_earned: .2f}\n")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    
    cd_balance = input("Enter your cd balance: ")

    cd_interest = input("Enter your interest rate: ")

    cd_maturity = input("Enter in the number of months: " )

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(float(cd_balance), float(cd_interest), int(cd_maturity))

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nCD Balance: ${updated_cd_balance: .2f} \nInterest Earned: ${interest_earned: .2f}\n\n")


    #print(f"{interest_earned}, {updated_cd_balance}")


if __name__ == "__main__":
    # Call the main function.
    main()

