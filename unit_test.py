import csv
from utils import delete_existing_report  # Utility function to delete an existing report, if any
from report_generation import generate_report  # Function to generate the inventory report
from IMS_simulation import run_simulation  # Function to run the inventory simulation

def check_report_correctness():
    """
    Validates the correctness of the inventory report by checking specific constraints.
    """
    file = "inventory_report_Tshirts.csv"  # Report file to validate

    # Open the CSV file and read its contents
    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # Read the header row
        data = list(reader)  # Read the remaining rows as data
    
    # Initialize variables for tracking totals and restock days
    total_restocked = 0
    total_sold = 0
    restock_days = set()
    
    # Iterate through each row in the report
    for row in data:
        day_str, sold_units, restocked_units, remaining_units = row  # Extract values
        day = int(day_str)  # Convert day to an integer
        
        # Check if the day is within the expected range (0-49)
        if day < 0 or day > 49:
            print(f"Error: Day {day} out of range in file {file}")
            return
        
        # Check if units exceed the maximum allowed value of 2000
        if int(restocked_units) > 2000 or int(remaining_units) > 2000:
            print(f"Error: Units exceed 2000 in file {file} on day {day}")
            return
        
        # Accumulate the total units restocked and sold
        total_restocked += int(restocked_units)
        total_sold += int(sold_units)
        
        # Track the days when restocking occurred
        if int(restocked_units) > 0:
            restock_days.add(day)
    
    # Check if restocking occurred on all expected days (every 7th day)
    for expected_restock_day in range(7, 51, 7):
        if expected_restock_day not in restock_days:
            print(f"Error: Missing restock on day {expected_restock_day} in file {file}")
            return
    
    # Validate the totals using the formula: total_restocked - total_sold - last_remaining_units == -2000
    last_remaining_units = int(data[-1][3])  # Remaining units on the last day
    if total_restocked - total_sold - last_remaining_units != -2000:
        print(f"Error: Totals do not match in file {file}")
        print(total_restocked - total_sold - last_remaining_units)  # Print discrepancy for debugging
        return
    
    # If all checks pass, print a success message
    print(f"ALL CHECKS PASSED :) for file {file}")

def report_check():
    """
    Main function to execute the inventory simulation, generate a report,
    and validate its correctness.
    """
    total_days = 50  # Total number of days to simulate
    inventory_records = []  # List to store inventory records during simulation

    # Delete any existing report to avoid conflicts
    delete_existing_report()

    # Clear the inventory records list to ensure a fresh start
    inventory_records.clear()

    # Run the inventory simulation for the specified number of days
    run_simulation(total_days, inventory_records)

    # Generate a report based on the simulation results
    generate_report(inventory_records)

    # Validate the generated report for correctness
    check_report_correctness()
