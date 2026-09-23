# Brief explanation of the program: Rainfall record

# Initialize total variables to keep track of the sum manually
total_inches = 0.0
total_cm = 0.0

# Ask user for the number of years and validate it is 1 or more
years = int(input("How many years are you recording rainfall for?: "))
while years < 1:
    years = int(input("Invalid. How many years are you recording rainfall for?: "))

# Loop through each year
for year in range(1, years + 1):
    # Ask for inches of rainfall and validate it is 0 or more
    inches = float(input(f"Enter inches of rainfall for year {year}: "))
    while inches < 0:
         inches = float(input(f"Invaild. Enter inches of rainfall for year {year}: "))
    
    # Calculate cm and update our running totals
    cm = inches * 2.54
    total_inches = total_inches + inches
    total_cm = total_cm + cm
    
    # Display the cm of rainfall formatted to 2 decimal places
    print(f"In cm, this is {cm:.2f}")
    
    # Determine and display the appropriate message based on cm
    if cm < 15:
        print("Low")
    elif cm <= 30:
        print("Moderate")
    else:
        print("High")

# Calculate averages manually
avg_inches = total_inches / years
avg_cm = total_cm / years

# Display final totals and averages formatted to 2 decimal places
print(f"Total inches of rainfall is {total_inches:.2f}")
print(f"Total cm of rainfall is {total_cm:.2f}")
print(f"Average rainfall in inches is {avg_inches:.2f}")
print(f"Average rainfall in cm is {avg_cm:.2f}")
