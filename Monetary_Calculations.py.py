# Menu-Driven Calculator
# This program handles conversions, bank fees, and income tax calculations.

def main():
    # Initial menu call
    user_selection = get_choice()
    
    # Main program loop - runs until the user selects '5'
    while user_selection != "5":
        
        # Option 1: Weight Conversion
        if user_selection == "1":
            lbs = float(input("Enter the weight in pounds: "))
            print(f"Weight in Kilograms is {convert_weight(lbs):.2f}")
            
        # Option 2: Volume Conversion
        elif user_selection == "2":
            gal = float(input("Enter the volume in gallons: "))
            print(f"Volume in Liters is {convert_volume(gal):.2f}")
            
        # Option 3: Bank Fee Calculation
        elif user_selection == "3":
            checks = int(input("What is the number of checks?: "))
            while checks < 1:
                checks = int(input("Invalid - try again - What is the number of checks?: "))
            
            fee = calculate_check_fee(checks)
            print(f"Your total fee from the bank is ${fee:.2f}")
            
        # Option 4: Income Tax Calculation
        elif user_selection == "4":
            salary = float(input("What is your income for the year?: "))
            while salary < 0:
                salary = float(input("invalid - try again - What is your income for the year?: "))
            
            status = input("What is your filing status, married or single?: ").lower()
            while status not in ["single", "married"]:
                status = input("Invalid - try again - What is your filing status, married or single?: ").lower()
            
            tax = calculate_income_tax(salary, status)
            print(f"Your taxes due are ${tax:.2f}")

        # Re-prompt at the end of the loop to check for the exit condition
        user_selection = get_choice()
        
    # This runs only after the loop finishes (user chose '5')
    print("Exiting...")
