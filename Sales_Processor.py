
# Brief explanation of the program: Sales Processor for car dealership 

# Initialize empty lists to store dealer data
names = []
sales = []
commissions = []

# Ask for the number of dealers and validate the input (1-20)
num_dealers = 0
while num_dealers < 1 or num_dealers > 20:
    num_dealers = int(input("Enter the number of dealers (1-20): "))

# Loop through the exact number of dealers requested
for i in range(num_dealers):
    # Empty print to create a clean line break safely
    print()
    
    # Ask for dealer's name and add to the list
    name = input(f"Enter the name for dealer {i + 1}: ")
    names.append(name)
    
    # Ask for sales amount and validate it is 0 or more
    sale_amount = -1.0
    while sale_amount < 0:
        sale_amount = float(input(f"Enter the sales amount for {name}: $"))
    
    # Store valid sale amount
    sales.append(sale_amount)
    
    # Calculate commission based on the sales tiers provided
    if sale_amount <= 5000:
        commission = sale_amount * 0.10
    elif sale_amount <= 15000:
        commission = sale_amount * 0.15
    else:
        commission = sale_amount * 0.20
        
    # Store the calculated commission
    commissions.append(commission)

# Calculate all the required statistics using allowed built-in functions
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sales = total_sales / len(sales)
total_commission = sum(commissions)

# Display the overall statistics formatted to 2 decimal places
print()
print("--- DEALERSHIP STATISTICS ---")
print(f"Total Sales: ${total_sales:.2f}")
print(f"Highest Sale: ${highest_sale:.2f}")
print(f"Lowest Sale: ${lowest_sale:.2f}")
print(f"Average Sales: ${average_sales:.2f}")
print(f"Total Commission: ${total_commission:.2f}")

# Display the initial Unsorted Dealer Report
print()
print("DEALER REPORT")
print(f"{'Dealers'} {'Sales'} {'Commission'}")
for i in range(len(names)):
    print(f"{names[i]} ${sales[i]:.2f} ${commissions[i]:.2f}")

# Perform a manual Bubble Sort to order by commission (ascending)
n = len(commissions)
for i in range(n):
    for j in range(0, n - i - 1):
        if commissions[j] > commissions[j + 1]:
            
            # Swap commissions
            temp_comm = commissions[j]
            commissions[j] = commissions[j + 1]
            commissions[j + 1] = temp_comm
            
            # Swap names
            temp_name = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp_name
            
            # Swap sales
            temp_sale = sales[j]
            sales[j] = sales[j + 1]
            sales[j + 1] = temp_sale

# Display the Sorted Dealer Report
print()
print("DEALER REPORT - Ordered by commission")
print(f"{'Dealers'} {'Sales'} {'Commission'}")
for i in range(len(names)):
    print(f"{names[i]} ${sales[i]:.2f} ${commissions[i]:.2f}")

# Search for a specific dealer by name
print()
print("--- DEALER SEARCH ---")
search_name = input("Enter the name of the dealer you want to search for: ")

# Check if the requested name exists in our names list
if search_name in names:
    idx = names.index(search_name)
    print(f"Dealer: {names[idx]}")
    print(f"Sales: ${sales[idx]:.2f}")
    print(f"Commission: ${commissions[idx]:.2f}")
else:
    print("This dealer does not exist.")

